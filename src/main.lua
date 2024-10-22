love.graphics.setDefaultFilter("nearest", "nearest")

local game = require("src.game")
local player = require("src.player")

function love.load()
    game.load()  -- Carrega o mapa e os objetos do jogo
    player.load() -- Carrega o jogador
end

function love.update(dt)
    player.update(dt)  -- Atualiza a posição do jogador
end

function love.draw()
    game.draw()    -- Desenha o mapa e os objetos
    player.draw()  -- Desenha o jogador
end

function useComputer()
    -- Chama o script Python que abre a interface
    os.execute("python3 scripts/open_tkinter_interface.py")

    -- Depois que o usuário finalizar, leia os dados
    local data = readData()
    if data then
        print("Usuário digitou: " .. data.user_input)
    end
end
