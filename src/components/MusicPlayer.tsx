import React, { useEffect, useRef, useState } from 'react';
import { Volume2, VolumeX, Music, Disc } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

interface MusicPlayerProps {
  isPlaying: boolean;
  onToggle: () => void;
  autoStartOnOpen?: boolean;
}

export const MusicPlayer: React.FC<MusicPlayerProps> = ({ isPlaying, onToggle }) => {
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const [hasInteracted, setHasInteracted] = useState(false);

  useEffect(() => {
    if (!audioRef.current) return;

    if (isPlaying) {
      const playPromise = audioRef.current.play();
      if (playPromise !== undefined) {
        playPromise.catch((err) => {
          console.warn('Audio playback waiting for user gesture:', err);
        });
      }
    } else {
      audioRef.current.pause();
    }
  }, [isPlaying]);

  return (
    <>
      {/* Hidden Audio Element */}
      <audio
        ref={audioRef}
        src="/assets/wedding_music.mp3"
        loop
        preload="auto"
      />

      {/* Floating Bottom-Right Music Controller */}
      <div className="fixed bottom-6 right-6 z-40">
        <motion.button
          onClick={onToggle}
          whileHover={{ scale: 1.08 }}
          whileTap={{ scale: 0.94 }}
          className="group relative flex items-center gap-2 p-2.5 sm:px-4 sm:py-2.5 rounded-full bg-gradient-to-r from-burgundy via-[#991535] to-burgundy text-white font-cinzel text-xs font-bold tracking-wider shadow-xl hover:shadow-gold-glow border border-gold/70 transition-all duration-300"
          title={isPlaying ? 'Pause Background Music' : 'Play Background Music'}
        >
          {/* Rotating Disc / Mandala Icon */}
          <div className="relative">
            <Disc
              className={`w-5 h-5 text-gold ${
                isPlaying ? 'animate-[spin_4s_linear_infinite]' : ''
              }`}
            />
            {isPlaying && (
              <span className="absolute -top-1 -right-1 w-2 h-2 rounded-full bg-emerald-400 animate-ping" />
            )}
          </div>

          <span className="hidden sm:inline">
            {isPlaying ? 'Shehnai & Sangeet' : 'Play Music'}
          </span>

          <div className="p-1 rounded-full bg-black/30">
            {isPlaying ? (
              <Volume2 className="w-3.5 h-3.5 text-gold" />
            ) : (
              <VolumeX className="w-3.5 h-3.5 text-white/70" />
            )}
          </div>
        </motion.button>
      </div>
    </>
  );
};
