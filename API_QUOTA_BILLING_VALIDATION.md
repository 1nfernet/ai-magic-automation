# Free.ai / CogVideoX API Quota & Billing Validation

Status: **BLOCKED — provider account and live API terms have not been independently verified.**

This checklist is the required gate before any live generation attempt. Earlier assessment notes mentioning a daily free-token allowance are unverified leads, not an approved budget or entitlement.

## Required evidence

Record the date checked, the exact official URL, and a short evidence excerpt for each item:

- [ ] Official API base URL and current API documentation.
- [ ] Authentication method and credential scopes.
- [ ] Whether CogVideoX is currently available through the documented API (exact model identifier).
- [ ] Free-tier entitlement: amount, reset period, eligibility, expiry, and whether it is promotional.
- [ ] Whether generation consumes tokens, credits, seconds, or another billable unit.
- [ ] Per-request cost for the intended resolution, duration, frame rate, and aspect ratio.
- [ ] Rate limits, concurrency limits, queue limits, and HTTP 429 behavior.
- [ ] Billing prerequisites, payment method requirements, auto-recharge behavior, and spending controls.
- [ ] Commercial-use rights and applicable content / output restrictions.
- [ ] Data retention and whether submitted prompts or assets may be used for training.

## Decision rules

1. Do not treat marketing claims, third-party summaries, or an undocumented dashboard balance as proof of a free allowance.
2. Do not add a payment method, enable auto-recharge, purchase credits, or accept paid terms as part of this validation.
3. Do not send a generation request until the exact model, endpoint, request schema, and maximum possible charge are documented.
4. If the provider cannot state a zero-cost test entitlement and a hard spending limit, keep live generation disabled.
5. Never commit API keys, access tokens, billing identifiers, or account screenshots containing personal data.

## First Flower Magic test (only after the gate passes)

- Use one short, non-sensitive Flower Magic prompt.
- Request portrait 9:16 output and the shortest supported duration.
- Confirm the request is within an explicitly documented free allowance or a separately approved hard budget.
- Capture request ID, model ID, status, elapsed time, returned dimensions, duration, and any usage/cost metadata.
- Verify the returned asset can be downloaded and played.
- Do not publish, schedule, or cross-post the result automatically.

## Acceptance criteria

The gate may be marked **PASS** only when all required evidence above is recorded and the test can be performed without unapproved spending. Otherwise keep the provider status **BLOCKED** and document the exact missing evidence.

## Current status

No provider account has been authenticated, no API key has been added, no payment has been authorized, and no live generation or publishing has been performed.
