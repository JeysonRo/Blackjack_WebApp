import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query"
import { chooseAction, getGameState, startGame } from "./api/game";
import type { GameState } from "./types/game";
import "./App.css"
import Actions from "./components/Actions"
import Menu from "./components/Menu";
import Players from "./components/Players";

function App() {
  const queryClient = useQueryClient();

  const gameStateQuery = useQuery({
    queryKey: ["game"],
    queryFn: getGameState,
  });


  const startGameMutation = useMutation({
    mutationFn: startGame,
    onSuccess: (data) => {
      queryClient.setQueryData(["game"], data);
    },
  });

  const actionMutation = useMutation({
    mutationFn: chooseAction,
    onSuccess: (data) => {
      queryClient.setQueryData(["game"], data);
    },
  });

  return (
    <div className="App">
      <header>
        <h1>Blackjack</h1>
      </header>

      <main>
        <section className="dealer">
          <h2>Dealer</h2>
          <div className="hand">
            {(gameStateQuery.isSuccess) && (<p>{gameStateQuery.data.dealer_hand}</p>)}
          </div>
        </section>

        {gameStateQuery.data && (
          <Actions gameState={gameStateQuery.data} actionMutation={actionMutation} /> /* component to show actions */
        )}
        
        <Players gameState={gameStateQuery.data}/>

        <Menu startGameMutation={startGameMutation} /> {/* Component for displaying Menu */}

        <div className="debug">
          {(gameStateQuery.isSuccess) && (
            <pre>
              {JSON.stringify(gameStateQuery.data, null, 2)}
            </pre>
          )}
        </div>
      </main>
    </div>
  );
}

export default App;