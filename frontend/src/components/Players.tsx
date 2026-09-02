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
                        {gameState.player_hands.length > 1 && (gameState.player_hands.slice(1).map((player, index) => (
                            <div className="hand" key={index}>
                                <h3>hand {index}</h3>

                                <Hand cards={player} />
                            </div>
                        )))}
                    </div>
                    <div className="selected">
                        <Hand cards={gameState.player_hands[0]} />
                    </div>
                    <div className="handlist">
                        {gameState.finished_hands.map((player, index) => (
                            <div className="hand" key={index}>
                                <h3>finished hand {index}</h3>

                                <Hand cards={player} />
                            </div>
                        ))}
                    </div>
                </div>
            )}
        </div>
    );
}
