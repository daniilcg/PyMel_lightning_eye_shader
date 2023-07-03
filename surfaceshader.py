import pymel.core as pm

def lightningShader(output, eyeColor, lightColor):
    result = pm.SurfaceShader(name="lightningShader")
    result.addAttr("eyeColor", at="float3")
    result.eyeColor.set(eyeColor)
    result.addAttr("lightColor", at="float3")
    result.lightColor.set(lightColor)
    result.outColor.connect(output)

    return result

# Usage example
shader = lightningShader(pm.PyNode('lightningShader_output'), (0.1, 0.1, 0.1), (1.0, 1.0, 1.0))
