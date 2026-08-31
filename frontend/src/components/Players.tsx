import type { GameState } from "../types/game";

type Props = {
    gameState: GameState | undefined;
}


export default function Players({ gameState }: Props) {
    return (
        <div>
            <h2>Player</h2>
            {gameState && (
                <div>
                    {gameState.player_hand.map((card: string, index: number) => (
                        <span key={index}>
                            {index > 0 && " | "}
                            {card}
                        </span>
                    ))}
                </div>
            )}
        </div>
    );
}
