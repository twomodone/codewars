def combat(health, damage):
    health -= damage
    if health > 0:
        return health
    return 0
