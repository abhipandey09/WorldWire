import React, { useRef, useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { Play, Pause, Film, Volume2, VolumeX, Maximize2, ChevronDown } from 'lucide-react';

interface WeddingFilmSectionProps {
  isPlayingSiteMusic?: boolean;
  onVideoPlay?: () => void;
  onVideoPause?: () => void;
}

export const WeddingFilmSection: React.FC<WeddingFilmSectionProps> = ({
  isPlayingSiteMusic = false,
  onVideoPlay,
  onVideoPause,
}) => {
  const videoRef = useRef<HTMLVideoElement | null>(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [isMuted, setIsMuted] = useState(false);

  // If outer site background music starts playing, automatically pause this video
  useEffect(() => {
    if (isPlayingSiteMusic && isPlaying && videoRef.current) {
      videoRef.current.pause();
      setIsPlaying(false);
    }
  }, [isPlayingSiteMusic]);

  const togglePlay = () => {
    if (!videoRef.current) return;
    if (isPlaying) {
      videoRef.current.pause();
      setIsPlaying(false);
      onVideoPause?.();
    } else {
      onVideoPlay?.();
      const playPromise = videoRef.current.play();
      if (playPromise !== undefined) {
        playPromise
          .then(() => {
            setIsPlaying(true);
          })
          .catch((err) => {
            console.warn('Video playback requires user gesture or muted policy:', err);
            if (videoRef.current) {
              videoRef.current.muted = true;
              setIsMuted(true);
              videoRef.current.play().then(() => setIsPlaying(true)).catch(() => {});
            }
          });
      }
    }
  };

  const toggleMute = () => {
    if (!videoRef.current) return;
    videoRef.current.muted = !isMuted;
    setIsMuted(!isMuted);
  };

  const handleFullscreen = () => {
    if (!videoRef.current) return;
    if (videoRef.current.requestFullscreen) {
      videoRef.current.requestFullscreen();
    }
  };

  return (
    <section id="film" className="relative py-20 bg-gradient-to-b from-[#1C0D11] via-[#2A1117] to-[#12070A] text-white overflow-hidden">
      {/* Golden Stage Glow */}
      <div className="absolute inset-0 pointer-events-none overflow-hidden">
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[340px] sm:w-[700px] h-[340px] sm:h-[500px] bg-gold/10 rounded-full blur-[90px] sm:blur-[140px]" />
      </div>

      <div className="relative z-10 max-w-4xl mx-auto px-4 sm:px-6 text-center">
        {/* Section Header */}
        <div className="mb-10">
          <div className="flex items-center justify-center gap-2 mb-2 text-gold font-serif font-bold text-sm tracking-widest uppercase">
            <Film className="w-4 h-4 text-gold" />
            <span>Cinematic Invitation Experience</span>
            <Film className="w-4 h-4 text-gold" />
          </div>

          <h2 className="font-serif font-bold text-3xl sm:text-5xl text-white tracking-tight">
            The Wedding Film
          </h2>

          <p className="font-cormorant italic text-base sm:text-lg text-gold/80 mt-2 max-w-xl mx-auto">
            Experience our animated destination wedding invitation, celebrating the beginning of our forever.
          </p>
        </div>

        {/* Video Player Frame with Gold Filigree Border */}
        <div className="relative w-fit mx-auto rounded-3xl overflow-hidden border-2 border-gold/70 shadow-2xl bg-black group">
          <div className="relative aspect-[9/16] h-[68vh] sm:h-[76vh] max-h-[720px] w-auto max-w-[92vw] flex items-center justify-center bg-black">
            <video
              ref={videoRef}
              src="/assets/Sakshi_Abhishek_Wedding.mp4"
              poster="/assets/ganesh.jpg"
              playsInline
              preload="metadata"
              onClick={togglePlay}
              onPlay={() => {
                setIsPlaying(true);
                onVideoPlay?.();
              }}
              onPause={() => {
                setIsPlaying(false);
                onVideoPause?.();
              }}
              onEnded={() => {
                setIsPlaying(false);
                onVideoPause?.();
              }}
              className="w-full h-full object-contain cursor-pointer"
            />

            {/* Play Overlay Button */}
            {!isPlaying && (
              <div
                onClick={togglePlay}
                className="absolute inset-0 bg-black/40 backdrop-blur-[2px] flex items-center justify-center cursor-pointer group-hover:bg-black/30 transition-all z-10"
              >
                <motion.button
                  whileHover={{ scale: 1.1 }}
                  whileTap={{ scale: 0.95 }}
                  className="w-20 h-20 rounded-full bg-gradient-to-tr from-burgundy to-gold p-0.5 shadow-gold-glow flex items-center justify-center"
                >
                  <div className="w-full h-full rounded-full bg-burgundy/90 flex items-center justify-center pl-1 border border-gold/60">
                    <Play className="w-9 h-9 text-gold fill-gold" />
                  </div>
                </motion.button>
              </div>
            )}

            {/* Video Controls Toolbar */}
            <div
              className={`absolute bottom-0 inset-x-0 p-4 bg-gradient-to-t from-black/90 via-black/50 to-transparent flex items-center justify-between transition-opacity z-20 ${
                isPlaying ? 'opacity-95 sm:opacity-0 sm:group-hover:opacity-100' : 'opacity-0 pointer-events-none'
              }`}
            >
              <div className="flex items-center gap-2">
                <button
                  onClick={togglePlay}
                  className="p-2 rounded-full bg-white/20 hover:bg-white/30 text-white transition-colors"
                >
                  {isPlaying ? <Pause className="w-4 h-4" /> : <Play className="w-4 h-4 fill-white" />}
                </button>
                <button
                  onClick={toggleMute}
                  className="p-2 rounded-full bg-white/20 hover:bg-white/30 text-white transition-colors"
                >
                  {isMuted ? <VolumeX className="w-4 h-4" /> : <Volume2 className="w-4 h-4" />}
                </button>
              </div>

              <button
                onClick={handleFullscreen}
                className="p-2 rounded-full bg-white/20 hover:bg-white/30 text-white transition-colors"
              >
                <Maximize2 className="w-4 h-4" />
              </button>
            </div>
          </div>
        </div>

        {/* Scroll Option to Next Section: Footer / Blessings */}
        <div className="mt-12 flex justify-center">
          <button
            onClick={() => document.querySelector('#footer')?.scrollIntoView({ behavior: 'smooth' })}
            className="flex flex-col items-center gap-1.5 text-gold/80 hover:text-gold transition-colors group cursor-pointer"
          >
            <span className="font-cinzel text-xs font-semibold tracking-widest uppercase">
              Closing Blessings &amp; Family Love
            </span>
            <ChevronDown className="w-4 h-4 animate-bounce text-gold" />
          </button>
        </div>
      </div>
    </section>
  );
};
