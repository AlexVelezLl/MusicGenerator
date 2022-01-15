import React, { useState } from "react";
import { Bars } from "react-loader-spinner";
import "react-loader-spinner/dist/loader/css/react-spinner-loader.css";

import MelodyPlayer from "../shared/MelodyPlayer";
import Select from "../shared/Select";
import { modes, notes } from "../../constants";
import { transformMidiToMp3 } from "../../services";
import { Slider, SliderThumbComponent } from "../shared/Slider";

import "./index.scss";

const SeedMusic = (props) => {
  const {
    setSeedName,
    setNote,
    setMode,
    temperature, 
    setTemperature,
  } = props;
  const [currentAudio, setCurrentAudio] = useState(null);
  const [loading, setLoading] = useState(false);
  const handleTempSliderChange = (_, newValue) => {
    setTemperature(newValue);
  };
  const handleTempInputChange = (event) => {
    setTemperature(event.target.value === "" ? "" : Number(event.target.value));
  };
  const handleTempBlur = () => {
    if (temperature < 10) {
      setTemperature(10);
    } else if (temperature > 100) {
      setTemperature(100);
    }
  };

  const handleOnSubmit = async () => {
    setLoading(true);
    const input_midi = document.getElementById("input-midi").files[0];
    const url_file = await transformMidiToMp3(input_midi);
    const seedName = url_file.split("/").pop().replace(".mp3", ".mid");
    setSeedName(seedName);
    setCurrentAudio(url_file);
    setLoading(false);
  };

  return (
    <section className="seed-music">
      <h2>Seed music</h2>
      <div className="seed-music-container">
        <div className="seed-music-options">
          <label htmlFor="input-midi" className="btn">
            <input 
              id="input-midi" 
              type="file" 
              onChange={handleOnSubmit} 
              accept=".mid"
            />
            Select midi file
          </label>
          <div className="key-note">
            <div>
              <div className="label">Note:</div>
              <Select 
                options={notes} 
                defaultValue={notes[0]} 
                onChange={setNote}
              />
            </div>
            <div>
              <div className="label">Mode:</div>
              <Select 
                options={modes} 
                defaultValue={modes[0]} 
                onChange={setMode}
              />
            </div>
          </div>
          <div className="temperature-container">
            <div className="label">Temperature:</div>
            <div className="temperature">
              <Slider
                value={temperature}
                onChange={handleTempSliderChange}
                aria-labelledby="input-slider"
                components={{ Thumb: SliderThumbComponent }}
                min={10}
                max={100}
              />
              <input
                value={temperature}
                onChange={handleTempInputChange}
                onBlur={handleTempBlur}
                step={10}
                min={10}
                max={100}
                type="number"
                aria-labelledby="input-slider"
              />
              <strong>%</strong>
            </div>
          </div>
        </div>
        <div className="seed-music-player">
          {
            loading &&
            <div
              className="loader"
            >
              <h2>Loading music...</h2>
              <div style={{ marginLeft: "40px" }}>
                <Bars
                  color="#4CC678"
                  height={100}
                  width={100}

                  visible={loading}
                />
              </div>
            </div>
          }
          {
            !loading && 
            currentAudio && 
            <MelodyPlayer audio={currentAudio} />
          }
        </div>
      </div>
    </section>
  );
};

export default SeedMusic;
