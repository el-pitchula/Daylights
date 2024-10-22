-- src/communication.lua
local json = require("dkjson")  -- Dependência JSON para Lua (instale via Luarocks ou inclua uma lib local)

-- Função para ler o arquivo JSON gerado pelo Python
function readData()
    local file = io.open("data/data.json", "r")
    if file then
        local content = file:read("*a")
        file:close()
        local data = json.decode(content)
        return data
    else
        print("Arquivo de dados não encontrado.")
        return nil
    end
end
