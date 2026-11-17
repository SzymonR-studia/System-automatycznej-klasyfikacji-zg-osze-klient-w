"""Simple rule-based baseline for the selected Banking77 intents."""

import re
from collections.abc import Iterable


KEYWORD_RULES = {
    "activate_my_card": (
        "activate my card", "activate card", "card activation", "activation code",
    ),
    "balance_not_updated_after_bank_transfer": (
        "balance not updated", "balance not changed after transfer",
        "transfer not reflected", "money not showing after transfer",
    ),
    "beneficiary_not_allowed": (
        "beneficiary not allowed", "cannot add beneficiary", "can't add beneficiary",
        "recipient not allowed",
    ),
    "cancel_transfer": (
        "cancel transfer", "cancel my transfer", "stop transfer", "abort transfer",
    ),
    "card_about_to_expire": (
        "card expiring", "card about to expire", "card expiry", "card expiration",
    ),
    "card_arrival": (
        "where is my card", "card has not arrived", "card hasn't arrived",
        "waiting for my card",
    ),
    "card_delivery_estimate": (
        "when will my card arrive", "how long for my card", "delivery estimate",
        "expected delivery date",
    ),
    "card_linking": (
        "link my card", "linking my card", "add card to app", "card in the app",
    ),
    "card_not_working": (
        "card not working", "card doesn't work", "card does not work",
        "card stopped working",
    ),
    "card_payment_fee_charged": (
        "card payment fee", "fee on card payment", "charged a fee for card",
        "card transaction fee",
    ),
    "card_payment_not_recognised": (
        "card payment not recognised", "don't recognise this card payment",
        "unauthorised card payment", "unknown card transaction",
    ),
    "card_payment_wrong_exchange_rate": (
        "wrong exchange rate on card", "card payment exchange rate",
        "wrong rate for card payment", "card charged wrong currency rate",
    ),
    "cash_withdrawal_charge": (
        "cash withdrawal charge", "atm withdrawal fee", "charged for cash withdrawal",
        "fee for withdrawing cash",
    ),
    "cash_withdrawal_not_recognised": (
        "cash withdrawal not recognised", "unrecognised atm withdrawal",
        "don't recognise this withdrawal", "unknown cash withdrawal",
    ),
    "change_pin": (
        "change my pin", "change pin", "update my pin", "new card pin",
    ),
    "declined_card_payment": (
        "card payment declined", "card was declined", "declined card payment",
        "card transaction declined",
    ),
    "declined_cash_withdrawal": (
        "cash withdrawal declined", "atm withdrawal declined", "cash withdrawal rejected",
        "couldn't withdraw cash",
    ),
    "declined_transfer": (
        "transfer declined", "declined bank transfer", "transfer was rejected",
        "bank transfer declined",
    ),
    "direct_debit_payment_not_recognised": (
        "direct debit not recognised", "unknown direct debit", "don't recognise this direct debit",
        "unrecognised direct debit payment",
    ),
    "extra_charge_on_statement": (
        "extra charge on statement", "unexpected charge on my statement",
        "unfamiliar charge on statement", "extra fee on statement",
    ),
    "failed_transfer": (
        "transfer failed", "failed bank transfer", "my transfer failed",
        "transfer was unsuccessful",
    ),
    "pending_card_payment": (
        "pending card payment", "card payment pending", "card transaction is pending",
        "card payment still pending",
    ),
    "pending_cash_withdrawal": (
        "pending cash withdrawal", "atm withdrawal pending", "cash withdrawal is pending",
        "atm transaction pending",
    ),
    "pending_top_up": (
        "pending top up", "top up pending", "top-up pending", "top up is pending",
    ),
    "pending_transfer": (
        "pending transfer", "transfer pending", "bank transfer is pending",
        "transfer still pending",
    ),
    "receiving_money": (
        "receive money", "receiving money", "someone sent me money", "money sent to me",
    ),
    "reverted_card_payment?": (
        "reverted card payment", "card payment reversed", "reversal of card payment",
        "card payment was reverted",
    ),
    "top_up_by_bank_transfer_charge": (
        "bank transfer top up fee", "charge for top up by bank transfer",
        "fee for bank transfer top up", "top up transfer charge",
    ),
    "top_up_failed": (
        "top up failed", "failed to top up", "top-up unsuccessful", "top up didn't work",
    ),
    "top_up_reverted": (
        "top up reverted", "top up reversed", "reverted top up", "top up was returned",
    ),
    "topping_up_by_card": (
        "top up by card", "top up with my card", "topping up by card",
        "add money using my card",
    ),
    "transaction_charged_twice": (
        "charged twice", "charged two times", "duplicate transaction",
        "same payment twice",
    ),
    "transfer_into_account": (
        "transfer into my account", "money into my account", "send money to my account",
        "pay into my account",
    ),
    "transfer_not_received_by_recipient": (
        "recipient has not received", "recipient hasn't received", "not received by recipient",
        "money not received by recipient",
    ),
    "transfer_timing": (
        "how long does a transfer take", "transfer timing", "when will transfer arrive",
        "how long for bank transfer",
    ),
}


def _predict_one(text: str, fallback_label: str) -> str:
    normalized_text = text.lower()
    scores = {}

    for label, keywords in KEYWORD_RULES.items():
        score = 0
        for keyword in keywords:
            pattern = rf"(?<!\w){re.escape(keyword)}(?!\w)"
            if re.search(pattern, normalized_text):
                score += len(keyword.split())
        if score:
            scores[label] = score

    if not scores:
        return fallback_label

    # Dict insertion order makes ties deterministic and easy to reproduce.
    return max(scores, key=scores.get)


def predict_keyword_baseline(
    texts: Iterable[str], fallback_label: str
) -> list[str]:
    """Predict intents using phrase rules, with a training-majority fallback."""
    return [_predict_one(text, fallback_label) for text in texts]