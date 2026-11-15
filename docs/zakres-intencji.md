# Zakres intencji projektu

## Wybrane kategorie

Projekt będzie klasyfikować zgłoszenia do 35 intencji z Banking77. Kategorie dobrano tak, aby obejmowały problemy z kartami, płatnościami, wypłatami, przelewami i doładowaniami.

Liczebności poniżej oznaczają liczbę przykładów w oryginalnym zbiorze treningowym przed filtrowaniem. Oryginalny zbiór testowy zawiera po 40 przykładów każdej intencji.

### Karty i dostęp do nich

| Intencja Banking77 | Przykłady treningowe |
|---|---:|
| `activate_my_card` | 159 |
| `card_about_to_expire` | 129 |
| `card_arrival` | 153 |
| `card_delivery_estimate` | 112 |
| `card_linking` | 139 |
| `card_not_working` | 112 |
| `change_pin` | 122 |

### Płatności i wypłaty

| Intencja Banking77 | Przykłady treningowe |
|---|---:|
| `card_payment_fee_charged` | 187 |
| `card_payment_not_recognised` | 168 |
| `card_payment_wrong_exchange_rate` | 167 |
| `declined_card_payment` | 153 |
| `pending_card_payment` | 143 |
| `reverted_card_payment?` | 129 |
| `cash_withdrawal_charge` | 177 |
| `cash_withdrawal_not_recognised` | 160 |
| `declined_cash_withdrawal` | 173 |
| `pending_cash_withdrawal` | 149 |
| `direct_debit_payment_not_recognised` | 182 |
| `transaction_charged_twice` | 172 |
| `extra_charge_on_statement` | 166 |

### Przelewy i wpływy

| Intencja Banking77 | Przykłady treningowe |
|---|---:|
| `balance_not_updated_after_bank_transfer` | 171 |
| `beneficiary_not_allowed` | 156 |
| `cancel_transfer` | 157 |
| `declined_transfer` | 133 |
| `failed_transfer` | 137 |
| `pending_transfer` | 115 |
| `receiving_money` | 162 |
| `transfer_into_account` | 171 |
| `transfer_not_received_by_recipient` | 128 |
| `transfer_timing` | 102 |

### Doładowania

| Intencja Banking77 | Przykłady treningowe |
|---|---:|
| `pending_top_up` | 148 |
| `top_up_by_bank_transfer_charge` | 114 |
| `top_up_failed` | 145 |
| `top_up_reverted` | 103 |
| `topping_up_by_card` | 175 |

## Wielkość wybranego podzbioru

- Liczba intencji: **35**.
- Zbiór treningowy: **5 169** przykładów.
- Zbiór testowy: **1 400** przykładów, po 40 na intencję.

## Źródło

Nazwy intencji i mapowanie etykiet pochodzą z [karty Banking77 na Hugging Face](https://huggingface.co/datasets/PolyAI/banking77#data-fields). Liczebności policzono na lokalnych plikach `data/raw/banking77_train.csv` i `data/raw/banking77_test.csv`.
