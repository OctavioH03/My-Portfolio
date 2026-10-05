import { Suspense, useRef } from "react";
import { Canvas } from "@react-three/fiber";
import { RoomLighting } from "./environment/RoomLighting";
import { OrbitControls, Grid } from "@react-three/drei";
import { Room } from "./environment/Room";
import * as THREE from 'three';
import { MonitorMNKMesh } from "./interactive_objects/monitor-about/MonitorMNKMesh";
import { PaperPlaneMesh } from "./interactive_objects/plane-contact/PaperPlaneMesh";
import { Camera } from "./Camera";
import { PostProcessing } from "./effects/PostProcessing";


export function Scene() {

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
                onCreated={({ gl }) => {
                    gl.setPixelRatio(window.devicePixelRatio);
                    gl.setSize(window.innerWidth, window.innerHeight);
                }}
            >
                <Suspense fallback={null}>
                    {/* DEBUGGING /DEV ONLY */}
                    {/* <OrbitControls /> */}
                    {/* <Grid args={[100, 100]} scale={0.1} rotation={[-Math.PI / 2, 0, 0]} side={THREE.DoubleSide} /> */}

                    <Camera
                        position={new THREE.Vector3(0, -3.65, -0.75)}
                        rotation={new THREE.Vector3(0.1, Math.PI, 0)}
                    />
                    <Room
                        position={new THREE.Vector3(0, -4.5, 0)}
                    />
                    {/* Interactive objects */}
                    <MonitorMNKMesh
                        position={new THREE.Vector3(0, -3.965, 0)}
                        rotation={new THREE.Vector3(0, Math.PI, 0)}
                    />
                    <PaperPlaneMesh
                        position={new THREE.Vector3(0.5, -3.885, -0.1)}
                        rotation={new THREE.Vector3(0, Math.PI / 2, 0)}
                        scale={0.1}
                    />
                    <RoomLighting
                        directionalLightPosition={new THREE.Vector3(0, 10, 100)}
                        pointLightPosition={new THREE.Vector3(0, -2, 0)}
                        targetPosition={new THREE.Vector3(0, -3, 0)}
                    />
                    {/* Post Processing */}
                    <PostProcessing />
                </Suspense>
            </Canvas>
        </div>
    )
}