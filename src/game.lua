local game = {}

-- Carregar os arquivos dos mapas
local map1 = require("maps.map1")
local map2 = require("maps.map2")

-- Função para converter coordenadas cartesianas para isométricas
function cartToIso(x, y)
    local isoX = (x - y) * 64 / 2  -- Usando a largura do tile como 64
    local isoY = (x + y) * 32 / 2  -- Usando a altura do tile como 32
    return isoX, isoY
end

function game.load()
    -- Inicializar o mapa e objetos aqui
    game.map = map1  -- Carrega o primeiro mapa
    game.objects = {
        {x = 3, y = 4, image = love.graphics.newImage("assets/images/object.png"), height = 64},
        {x = 6, y = 7, image = love.graphics.newImage("assets/images/object.png"), height = 64}
    }
end

function game.draw()
    -- Desenhar o chão do mapa (grid isométrico)
    for y = 0, game.map.height - 1 do
        for x = 0, game.map.width - 1 do
            local isoX, isoY = cartToIso(x, y)
            love.graphics.draw(game.map.tileImage, isoX, isoY)
        end
    end

    -- Desenhar os objetos na ordem correta
    for _, obj in ipairs(game.objects) do
        local isoX, isoY = cartToIso(obj.x, obj.y)
        love.graphics.draw(obj.image, isoX, isoY - obj.height)
    end
end

return game
