#!/usr/bin/env python3
"""Parse email files (.eml/.mbox) to extract boss communications."""

import argparse
import email
import mailbox
import sys
from email.header import decode_header
from pathlib import Path


def decode_str(s):
    """Decode email header string."""
    if s is None:
        return ""
    decoded = decode_header(s)
    parts = []
    for content, charset in decoded:
        if isinstance(content, bytes):
            parts.append(content.decode(charset or "utf-8", errors="replace"))
        else:
            parts.append(content)
    return " ".join(parts)


def extract_body(msg):
    """Extract text body from email message."""
    if msg.is_multipart():
        for part in msg.walk():
            ct = part.get_content_type()
            if ct == "text/plain":
                payload = part.get_payload(decode=True)
                charset = part.get_content_charset() or "utf-8"
                return payload.decode(charset, errors="replace")
    else:
        payload = msg.get_payload(decode=True)
        if payload:
            charset = msg.get_content_charset() or "utf-8"
            return payload.decode(charset, errors="replace")
    return ""


def parse_eml(file_path: str, target: str) -> list:
    """Parse a single .eml file."""
    with open(file_path, "rb") as f:
        msg = email.message_from_binary_file(f)

    sender = decode_str(msg.get("From", ""))
    if target.lower() not in sender.lower():
        return []

    return [{
        "from": sender,
        "to": decode_str(msg.get("To", "")),
        "subject": decode_str(msg.get("Subject", "")),
        "date": decode_str(msg.get("Date", "")),
        "body": extract_body(msg),
    }]


def parse_mbox(file_path: str, target: str) -> list:
    """Parse an mbox file."""
    mbox = mailbox.mbox(file_path)
    results = []
    for msg in mbox:
        sender = decode_str(msg.get("From", ""))
        if target.lower() in sender.lower():
            results.append({
                "from": sender,
                "to": decode_str(msg.get("To", "")),
                "subject": decode_str(msg.get("Subject", "")),
                "date": decode_str(msg.get("Date", "")),
                "body": extract_body(msg),
            })
    return results


def main():
    parser = argparse.ArgumentParser(description="Parse boss emails")
    parser.add_argument("--file", required=True, help="Path to .eml or .mbox file")
    parser.add_argument("--target", required=True, help="Boss name to filter by")
    parser.add_argument("--output", required=True, help="Output file path")
    args = parser.parse_args()

    path = Path(args.file)
    if not path.exists():
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)

    if path.suffix == ".mbox":
        emails = parse_mbox(str(path), args.target)
    else:
        emails = parse_eml(str(path), args.target)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(f"# Emails from {args.target}\n\n")
        f.write(f"Total: {len(emails)} emails\n\n")
        for i, e in enumerate(emails, 1):
            f.write(f"---\n## Email {i}\n")
            f.write(f"- From: {e['from']}\n")
            f.write(f"- To: {e['to']}\n")
            f.write(f"- Subject: {e['subject']}\n")
            f.write(f"- Date: {e['date']}\n\n")
            f.write(f"{e['body']}\n\n")

    print(f"Parsed {len(emails)} emails from {args.target} → {args.output}")


if __name__ == "__main__":
    main()
