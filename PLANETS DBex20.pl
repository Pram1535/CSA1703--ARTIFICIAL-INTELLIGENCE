orbits(mars,sun).
orbits(jupiter,sun).
orbits(earth,moon).
orbits(earth,sun).
orbits(denimol,mars).
orbits(jupiter,sun).
planent(P):-orbits(P,sun).
satellite(S):-satellite(S,P),planent(P)
