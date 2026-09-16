import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query"
import { chooseAction, getGameState, startGame } from "./api/game";
import { useState } from "react";
import "./App.css"
import Actions from "./components/Actions"
import Menu from "./components/Menu";
import Players from "./components/Players";
import Hand from "./components/Hand";

function App() {
  const [settingsOpen, setSettingsOpen] = useState(false);
  const [dealerH17, setDealerH17] = useState(true);
  // localStorage.setItem()

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

      <button className="settings-button" onClick={() => setSettingsOpen(true)}>Settings</button>
      {settingsOpen && (
        <div className="settings-panel">
          <button onClick={() => setSettingsOpen(false)}>✕</button>
          <h2>Settings</h2>

          {/* put settings here */}
          {/* <SettingsMenu/> */}

        </div>
      )}

      <main>
        <Menu startGameMutation={startGameMutation} />

        <section className="dealer">
          <h2>Dealer</h2>
          {gameStateQuery.data && (
            <Hand cards={gameStateQuery.data.dealer_hand}/>
          )}
        </section>

        <Players gameState={gameStateQuery.data}/>
        
        {gameStateQuery.data && (
          <Actions gameState={gameStateQuery.data} actionMutation={actionMutation} /> /* component to show actions */
        )}

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