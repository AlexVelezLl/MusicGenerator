import React, { useRef, useState } from "react";
import { Media, Player, controls } from "react-media-player";

import "./MelodyPlayer.scss";
var GifPlayer = require("react-gif-player");
const {
  PlayPause,
  CurrentTime,
  Progress,
  SeekBar,
  Duration,
  MuteUnmute,
  Volume,
  Fullscreen,
} = controls;

let pauseGif;

const MelodyPlayer = (props) => {
  const [playing, setPlaying] = useState(true);
  
  const ref = useRef();
  const player = useRef();

  const handlePlayPause = () => {
    setPlaying(!playing);
    const gifPlayer = ref.current.children[0];
    gifPlayer.click();
  };

  return (
    <div>
      <Media>
        <div className="media">
          <div className="media-player">
            <div
              ref={ref}
              style={{
                pointerEvents: "none",
              }}
            >
              <GifPlayer
                gif="music-bg.gif"
                pauseRef={(pause) => {
                  pauseGif = pause;
                }}
                className="background-image-gif"
              />
            </div>

            <Player
              src={props.audio}
              onPlay={handlePlayPause}
              onPause={handlePlayPause}
              ref={player}
            />
          </div>
          <div className="media-controls">
            <PlayPause className="media-control--play-pause" />

            <CurrentTime className="media-control media-control--current-time" />
            <div className="media-control-group media-control-group--seek">
              <Progress className="media-control media-control--progress" />
              <SeekBar className="media-control media-control--seekbar" />
            </div>
            <Duration className="media-control media-control--duration" />
            <Volume className="media-control media-control--volume" />
          </div>
        </div>
      </Media>
    </div>
  );
};

export default MelodyPlayer;
