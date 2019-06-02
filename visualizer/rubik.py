
rgw = flu = 0 # (0-th cubie; front face)
gwr = luf = 1 # (0-th cubie; left face)
wrg = ufl = 2 # (0-th cubie; up face)

rwb = fur = 3 # (1-st cubie; front face)
wbr = urf = 4 # (1-st cubie; up face)
brw = rfu = 5 # (1-st cubie; right face)

ryg = fdl = 6 # (2-nd cubie; front face)
ygr = dlf = 7 # (2-nd cubie; down face)
gry = lfd = 8 # (2-nd cubie; left face)

rby = frd = 9 #  (3-rd cubie; front face)
byr = rdf = 10 # (3-rd cubie; right face)
yrb = dfr = 11 # (3-rd cubie; down face)

owg = bul = 12 # (4-th cubie; back face)
wgo = ulb = 13 # (4-th cubie; up face)
gow = lbu = 14 # (4-th cubie; left face)

obw = bru = 15 # (5-th cubie; back face)
bwo = rub = 16 # (5-th cubie; right face)
wob = ubr = 17 # (5-th cubie; up face)

ogy = bld = 18 # (6-th cubie; back face)
gyo = ldb = 19 # (6-th cubie; left face)
yog = dbl = 20 # (6-th cubie; down face)

oyb = bdr = 21 # (7-th cubie; back face)
ybo = drb = 22 # (7-th cubie; down face)
boy = rbd = 23 # (7-th cubie; right face)


####################################################
### Permutation operations
####################################################

def perm_apply(perm, position):
    """
    Apply permutation perm to a list position (e.g. of faces).
    Face in position p[i] moves to position i.
    """
    return tuple([position[i] for i in perm])

def perm_inverse(p):
    """
    Return the inverse of permutation p.
    """
    n = len(p)
    q = [0]*n
    for i in range(n):
        q[p[i]] = i
    return tuple(q)

def perm_to_string(p):
    """
    Convert p to string, slightly more compact
    than listprinting.
    """
    s = "("
    for x in p: s = s + "%2d "%x
    s += ")"
    return s

# Identity: equal to (0, 1, 2, ..., 23).
I = (flu, luf, ufl, fur, urf, rfu, fdl, dlf, lfd, frd, rdf, dfr,     bul, ulb, lbu, bru, rub, ubr, bld, ldb, dbl, bdr, drb, rbd)


# Front face rotated clockwise.
F = (fdl, dlf, lfd, flu, luf, ufl, frd, rdf, dfr, fur, urf, rfu, 
     bul, ulb, lbu, bru, rub, ubr, bld, ldb, dbl, bdr, drb, rbd)
# Front face rotated counter-clockwise.
Fi = perm_inverse(F)

# Left face rotated clockwise.
L = (ulb, lbu, bul, fur, urf, rfu, ufl, flu, luf, frd, rdf, dfr,
     dbl, bld, ldb, bru, rub, ubr, dlf, lfd, fdl, bdr, drb, rbd)
# Left face rotated counter-clockwise.
Li = perm_inverse(L)

# Upper face rotated clockwise.
U = (rfu, fur, urf, rub, ubr, bru, fdl, dlf, lfd, frd, rdf, dfr,
     luf, ufl, flu, lbu, bul, ulb, bld, ldb, dbl, bdr, drb, rbd)
# Upper face rotated counter-clockwise.
Ui = perm_inverse(U)

# All 6 possible moves (assuming that the lower-bottom-right cubie
# stays fixed).
quarter_twists = (F, Fi, L, Li, U, Ui)

quarter_twists_names = {}
quarter_twists_names[F] = 'F'
quarter_twists_names[Fi] = 'Fi'
quarter_twists_names[L] = 'L'
quarter_twists_names[Li] = 'Li'
quarter_twists_names[U] = 'U'
quarter_twists_names[Ui] = 'Ui'

def input_configuration():
    """
    Prompts a user to input the current configuration of the cube, and
    translates that into a permutation.
    """
    position = [-1]*24

    cubie = raw_input("""
    Look for the cubie with yellow, blue, and orange faces (it has the
    Rubiks mark). Put this cubie in the lower-back-right corner with
    the yellow face down. We will call this cubie #7.

    Now look at the cubie in the upper-front-left corner. We will call
    this cubie #0. Starting with its front face, and going clockwise,
    input the colors of the faces (e.g. yob, if the colors are yellow,
    orange, and blue):
    cubie #0: """)
    position[0] = eval(cubie)
    position[1] = eval(cubie[1:] + cubie[0])
    position[2] = eval(cubie[2] + cubie[:2])
    cubie = raw_input("""
    Now enter cubie #1, which is to the right of cubie #0, again
    starting with the front face and going clockwise:
    cubie #1: """)
    position[3] = eval(cubie)
    position[4] = eval(cubie[1:] + cubie[0])
    position[5] = eval(cubie[2] + cubie[:2])
    cubie = raw_input("""
    Now enter cubie #2, which is beneath cubie #0:
    cubie #2: """)
    position[6] = eval(cubie)
    position[7] = eval(cubie[1:] + cubie[0])
    position[8] = eval(cubie[2] + cubie[:2])
    cubie = raw_input("""
    Now enter cubie #3, to the right of cubie #2:
    cubie #3: """)
    position[9] = eval(cubie)
    position[10] = eval(cubie[1:] + cubie[0])
    position[11] = eval(cubie[2] + cubie[:2])
    cubie = raw_input("""
    Now enter cubie #4, which is behind cubie #0. Start with the back
    face, and go clockwise:
    cubie #4: """)
    position[12] = eval(cubie)
    position[13] = eval(cubie[1:] + cubie[0])
    position[14] = eval(cubie[2] + cubie[:2])
    cubie = raw_input("""
    Now enter cubie #5, which is to the right of cubie #4:
    cubie #5: """)
    position[15] = eval(cubie)
    position[16] = eval(cubie[1:] + cubie[0])
    position[17] = eval(cubie[2] + cubie[:2])
    cubie = raw_input("""
    Now enter cubie #6, which is beneath cubie #4:
    cubie #6: """)
    position[18] = eval(cubie)
    position[19] = eval(cubie[1:] + cubie[0])
    position[20] = eval(cubie[2] + cubie[:2])
    print("""We already know cubie #7, so we're done.""")
    cubie = 'oyb'
    position[21] = eval(cubie)
    position[22] = eval(cubie[1:] + cubie[0])
    position[23] = eval(cubie[2] + cubie[:2])

    return tuple(position)
