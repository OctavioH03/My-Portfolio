# You always need 3 objects
- Scene
- Camera
- Render

## Scene
- like a containter for all your objects, cameras, and lights

## Camera
- used to look inside a scene
- Perspective Camera
    - meant to mimic human POV
    - PARAMS
        - FOV
        - Aspect Ratio --> windows.innerWidth / windows.innerHeight
        - Last 2 args for VIEW FRUSTUM

## Renderer
- draws what the visuals of the scene
- args --> canvas: document.querySelector('#bg')

# Dependencies
`npm install three @react-three/fiber @react-three/drei @react-three/postprocessing gsap`
`npm install -D @types/three`
## Three
- used to making the 3d scene objects
## React Three Fiber (R3F)
- allows me to overlay react components onto three js canvas
## React Three Drei
- utilities for R3F
- i.e. Environment, OrbitControls, useGLTF, HTML
## GSAP
- handles all camera tweening to make smoother transitions