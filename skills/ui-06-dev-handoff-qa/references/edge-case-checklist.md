# Edge Case Checklist

Per screen, define behavior for every applicable case. State "N/A + why" when not applicable.

## Data
- [ ] Empty state (first use, zero results)
- [ ] Single item vs 1000 items (pagination/virtualization expectation)
- [ ] Long content: names, MM strings (+30%), large amounts, long emails
- [ ] Stale data / concurrent edit by another user

## Network
- [ ] Offline at load / offline mid-action (esp. booking, payment)
- [ ] Slow network: skeleton vs spinner, timeout copy, retry
- [ ] Partial failure (one of several requests fails)

## Input
- [ ] Validation errors: inline, on which event, error copy
- [ ] Double-tap / double-submit protection
- [ ] Paste, autofill, keyboard types (numeric for phone/amount)

## Permissions & auth
- [ ] Permission denied (camera for KYC, location)
- [ ] Session expired mid-flow (progress preserved?)
- [ ] Feature not available for user's plan/region

## Money & legal (Car Share, Easy Lease)
- [ ] Payment failure at each step, refund messaging
- [ ] Confirmation before irreversible legal/financial action (WCAG 3.3.4)
