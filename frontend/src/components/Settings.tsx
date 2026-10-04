interface SettingsProps {
    dealerH17: boolean;
    setDealerH17: React.Dispatch<React.SetStateAction<boolean>>;
}

export default function Settings({dealerH17, setDealerH17,}: SettingsProps) {
    return (
    <div className="setting">
        <span>Dealer hits soft 17</span>

        <button
        className={`toggle ${dealerH17 ? "active" : ""}`}
        onClick={() => setDealerH17(!dealerH17)}
        >
        <span className="toggle-knob" />
        </button>

        <span>{dealerH17 ? "H17" : "S17"}</span>
    </div>
    );
}