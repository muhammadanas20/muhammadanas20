# Agents & MCP interview extras

**Q. Plan-and-execute vs ReAct?**  
Plan first is readable but brittle; ReAct adapts. Graphs can encode either.

**Q. How do you eval an agent?**  
Trajectory: expected tools, order, no extras, final answer. Golden paths + adversarial.

**Q. MCP vs OpenAPI?**  
OpenAPI = HTTP for any client. MCP = tools/resources for model hosts. You can wrap OpenAPI with MCP.

**Q. Why stderr in MCP stdio servers?**  
Stdout is the protocol.

**Q. Destructive MCP tools?**  
Client approval UX + split read/write servers + OS user sandbox.
