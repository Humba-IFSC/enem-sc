import subprocess
import json
import sys
import time

def call_mcp_method(server_cmd, server_args, method, params, id=1):
    process = subprocess.Popen(
        [server_cmd] + server_args,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )
    
    # helper to send and receive
    def send_recv(meth, par, msg_id, is_notification=False):
        req = {
            "jsonrpc": "2.0",
            "method": meth,
            "params": par
        }
        if not is_notification:
            req["id"] = msg_id
            
        print(f"DEBUG SEND: {meth}", file=sys.stderr)
        process.stdin.write(json.dumps(req) + "\n")
        process.stdin.flush()
        
        if is_notification:
            return None
            
        while True:
            line = process.stdout.readline()
            if not line:
                break
            print(f"DEBUG OUT: {line.strip()}", file=sys.stderr)
            try:
                response = json.loads(line)
                if response.get("id") == msg_id:
                    return response
            except:
                continue
        return None

    # Handshake
    init_params = {
        "protocolVersion": "2024-11-05",
        "capabilities": {},
        "clientInfo": {"name": "shadow-client", "version": "1.0.0"}
    }
    init_res = send_recv("initialize", init_params, 0)
    if not init_res:
        process.terminate()
        return {"error": "Handshake failed"}
    
    send_recv("notifications/initialized", {}, None, is_notification=True)
    
    # Actual Method call
    result = send_recv(method, params, id)
    process.terminate()
    return result

if __name__ == "__main__":
    config_path = "/home/humba/.config/notebooklm-mcp/notebooklm-config.json"
    server_cmd = "/home/humba/Documentos/Meus_Projetos/notebooklm-mcp-fix/.venv/bin/notebooklm-mcp"
    server_args = ["--config", config_path, "server"]
    
    if len(sys.argv) < 2:
        # Just list tools if no message
        result = call_mcp_method(server_cmd, server_args, "tools/list", {})
        print(json.dumps(result.get("result", result), indent=2))
        sys.exit(0)
        
    message = sys.argv[1]
    call_params = {
        "name": "chat_with_notebook",
        "arguments": {"request": {"message": message}}
    }
    result = call_mcp_method(server_cmd, server_args, "tools/call", call_params)
    if "result" in result:
        print(json.dumps(result["result"], indent=2))
    else:
        print(json.dumps(result, indent=2))
