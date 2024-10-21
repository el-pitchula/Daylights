local player = {}

function player.load()
    player.image = love.graphics.newImage("assets/images/player.png")
    player.x = 5
    player.y = 5
    player.height = 32
    player.speed = 3
end

function player.update(dt)
    if love.keyboard.isDown("up") then
        player.y = player.y - player.speed * dt
    elseif love.keyboard.isDown("down") then
        player.y = player.y + player.speed * dt
    end

    if love.keyboard.isDown("left") then
        player.x = player.x - player.speed * dt
    elseif love.keyboard.isDown("right") then
        player.x = player.x + player.speed * dt
    end
end

function player.draw()
    local isoX, isoY = cartToIso(player.x, player.y)
    love.graphics.draw(player.image, isoX, isoY - player.height)
end

return player
