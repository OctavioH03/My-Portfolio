import { PerspectiveCamera } from "@react-three/drei";
import { Vector3 } from "three";

export function Camera({ position, rotation }: { position: Vector3, rotation: Vector3 }) {
    return (
        <PerspectiveCamera 
            makeDefault
            manual={false} // making it manual will stop auto responsiveness
            position={position}
            fov={60} 
            near={0.1}
            far={200}
            rotation={[rotation.x, rotation.y, rotation.z]}

        />
    )
}