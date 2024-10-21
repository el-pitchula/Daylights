local game = require("src.game")

function love.load()
    game.load()  -- Inicializa o jogo
end

function love.update(dt)
    game.update(dt)  -- Atualiza o estado do jogo
end

function love.draw()
    game.draw()  -- Desenha o jogo
end

function love.keypressed(key)
    game.keypressed(key)  -- Checa interações com o teclado
end
