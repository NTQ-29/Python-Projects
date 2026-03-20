import imaplib
import email
from email.header import decode_header

# --- CONFIG ---
EMAIL = "ENTER EMAIL HERE"
APP_PASSWORD = "**** **** **** ****"  # Your 16-char app password
SPAM_KEYWORDS = ["winner", "free money", "click here", "urgent", "help wanted", "verify your account"]

# --- CONNECT ---
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(EMAIL, APP_PASSWORD)

# --- SELECT INBOX ---
mail.select("inbox")

# --- SEARCH FOR EMAILS ---
# "ALL" fetches everything. You can also use "UNSEEN" for unread only.
status, messages = mail.search(None, "ALL")
email_ids = messages[0].split()

print(f"Found {len(email_ids)} emails. Scanning...\n")

flagged = []

# --- LOOP THROUGH EMAILS ---
# We'll just check the last 20 so it doesn't take forever
for email_id in email_ids[-20:]:
    status, msg_data = mail.fetch(email_id, "(RFC822)")

    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])

            # Decode subject line
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding or "utf-8")

            sender = msg.get("From")

            # Get body text
            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True).decode("utf-8", errors="ignore")
                        break
            else:
                body = msg.get_payload(decode=True).decode("utf-8", errors="ignore")

            # Check for spam keywords
            combined = (subject + " " + body).lower()
            hits = [kw for kw in SPAM_KEYWORDS if kw in combined]

            if hits:
                flagged.append({
                    "from": sender,
                    "subject": subject,
                    "keywords_found": hits
                })

# --- REPORT ---
print(f"=== SPAM SCAN RESULTS ===")
print(f"Emails scanned: 20")
print(f"Flagged: {len(flagged)}\n")

for item in flagged:
    print(f"FROM: {item['from']}")
    print(f"SUBJECT: {item['subject']}")
    print(f"KEYWORDS: {', '.join(item['keywords_found'])}")
    print("-" * 40)

mail.logout()
