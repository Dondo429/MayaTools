import pymel.core as pm


###select curve first then shape

def jumpOnCurve(startFrame, numberOfFrames, curv, shap):
    n = numberOfFrames
#    fj = frameJump
    st = startFrame
    ff = st + n

    sel = pm.ls(sl=True)
    print(sel)

    shape = pm.ls(shap+"Ctrl")[0]
    pm.parentConstraint(shape, shap)
    pm.pathAnimation(shape, c = curv, stu = startFrame, etu = ff, follow = True)


    currentFrame = st
    cx = pm.getAttr(shape+'.translateX')
    cy = pm.getAttr(shape+'.translateY')
    cz = pm.getAttr(shape+'.translateZ')
    i = 1
    print(pm.getAttr(shape+'.translate'))
    pm.select(clear = True)
    pm.select(shape, add=True)

#    while currentFrame <= ff:
#        pm.currentTime(currentFrame)
#        while i < fj:
#            pm.setKeyframe(t = currentFrame + i, v = pm.xform(shape, q = True, tx = True), at = 'translateX')
#            pm.setKeyframe(t = currentFrame + i, v = pm.xform(shape, q = True, ty = True), at = 'translateY')
#            pm.setKeyframe(t = currentFrame + i, v = pm.xform(shape, q = True, tz = True), at = 'translateZ')
#            pm.setKeyframe(attribute = 'translate', time = currentFrame + i)
#            print(pm.xform(shape, q = True, t = True))
#            print('i = ' + str(i))
#            i = i + 1
#        i = 1
#        print(currentFrame)
#        print(pm.xform(shape, q = True, t = True))
#        currentFrame = currentFrame + fj
    

def pConstrain(shape):
    pm.circle(c = pm.xform(shape, q = True, t = True), n = shape+'Ctrl')
    pm.makeIdentity(apply = True, t = 1, r = 1, s = 1, n = 0)


sel = pm.ls(sl = True)
shape = sel[1]
curv = sel[0]
pConstrain(shape)
jumpOnCurve(1, 30, curv, shape)
