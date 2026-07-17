import { Suspense, useRef } from "react";
import { Canvas } from "@react-three/fiber";
import { RoomLighting } from "./environment/RoomLighting";
import { OrbitControls } from "@react-three/drei";
import { Room } from "./environment/Room";
import * as THREE from 'three';


export function Scene() {

    const roomRef = useRef<THREE.Object3D>(null!);

    return (
        <div className="w-full h-full pt-16">
            <Canvas
                shadows="soft"
                camera={{
                    fov: 45,
                    near: 0.1,
                    far: 200,
                    position: [0, -1, 10],
                }}
                gl={{
                    antialias: true,  
                    toneMappingExposure: 1.2,
                    alpha: true,
                }}
                style={{
                    position: 'absolute',
                    inset: 0,
                }}
                onCreated={({ gl, camera }) => {
                    gl.setPixelRatio(window.devicePixelRatio);
                    gl.setSize(window.innerWidth, window.innerHeight);
                    camera.lookAt(0, -3, 0);
                }}
            >
                <Suspense fallback={null}>
                    <Room position={new THREE.Vector3(0, -4.5, 0)} />
                    {/* Interactive objects */}                    
                    <RoomLighting position={new THREE.Vector3(0, 10, 100)} targetPosition={new THREE.Vector3(0, -3, 0)} />
                    {/* Post Processing */}

                    {/* DEBUGGING /DEV ONLY */}
                    {/* <OrbitControls /> */}
                </Suspense>
            </Canvas>
        </div>
    )
}