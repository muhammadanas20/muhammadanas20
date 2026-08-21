# Design: customer support bot

Tools: `get_order`, `get_policy` (RAG), `create_ticket`. Refunds = HITL.

Route chit-chat vs policy vs order.

Abuse: injection asking to refund. RBAC.

Latency: cached policies, stream tokens.

Cost: cheaper model for classify/route.

Failure: tool down → apologize + ticket.
