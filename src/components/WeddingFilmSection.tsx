import React, { useRef, useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { Play, Pause, Film, Volume2, VolumeX, Maximize2 } from 'lucide-react';

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
      videoRef.current.play();
      setIsPlaying(true);
      onVideoPlay?.();
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
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[700px] h-[500px] bg-gold/10 rounded-full blur-[140px] pointer-events-none" />

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
        <div className="relative max-w-sm sm:max-w-md mx-auto rounded-3xl overflow-hidden border-2 border-gold/70 shadow-2xl bg-black group">
          <div className="relative aspect-[9/16] max-h-[75vh] w-full flex items-center justify-center">
            <video
              ref={videoRef}
              src="/assets/wedding_film.mp4"
              poster="/assets/cards/Slide_01_Welcome.jpg"
              playsInline
              preload="metadata"
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
              className="w-full h-full object-cover"
            />

            {/* Play Overlay Button */}
            {!isPlaying && (
              <div
                onClick={togglePlay}
                className="absolute inset-0 bg-black/40 backdrop-blur-[2px] flex items-center justify-center cursor-pointer group-hover:bg-black/30 transition-all"
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
            <div className="absolute bottom-0 inset-x-0 p-4 bg-gradient-to-t from-black/90 via-black/50 to-transparent flex items-center justify-between opacity-0 group-hover:opacity-100 transition-opacity">
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

        <p className="font-cormorant italic text-xs sm:text-sm text-gold/70 mt-4">
          Featuring &ldquo;Mangal Rang&rdquo; &bull; Directed for Sakshi &amp; Abhishek
        </p>
      </div>
    </section>
  );
};
