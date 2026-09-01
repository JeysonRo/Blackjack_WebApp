import type { GameState } from "../types/game";

type Props = {
    gameState: GameState | undefined;
}


export default function Players({ gameState }: Props) {
    return (
        <div className="players">
            <h2>Player</h2>
            {gameState && (
                <div>
                    {/* <Hand cards=/> */}
                    <div className="hand">
                        {gameState.player_hands[0].map((card: string, index: number) => (
                            <span key={index}>
                                {index > 0 && " | "}
                                {card}
                            </span>
                        ))}
                    </div>
                </div>
            )}
        </div>
    );
}
