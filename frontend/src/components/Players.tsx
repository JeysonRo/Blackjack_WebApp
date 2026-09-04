import type { GameState } from "../types/game";
import Hand from "./Hand";

type Props = {
    gameState: GameState | undefined;
}


export default function Players({ gameState }: Props) {
    return (
        <div className="player">
            <h2>Players</h2>
            {gameState && (
                <div className="handgroup">
                    <div className="handlist">
                        {(gameState.player_hands.slice(1).map((player, index) => (
                            <div className="hand" key={index}>
                                <Hand cards={player} />
                            </div>
                        )))}
                    </div>
                    {gameState.player_hands.length > 0 &&
                        <div className="selected">
                            <Hand cards={gameState.player_hands[0]} />
                        </div>
                    }

                    <div className="handlist">
                        {gameState.finished_hands.map((player, index) => (
                            <div className="hand" key={index}>
                                <Hand cards={player} />
                            </div>
                        ))}
                    </div>
                </div>
            )}
        </div>
    );
}
