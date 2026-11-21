import React, { useState, useRef, useEffect } from 'react';
import { InvitationCover } from './components/InvitationCover';
import { PetalBackground } from './components/PetalBackground';
import { Navbar } from './components/Navbar';
import { Hero } from './components/Hero';
import { FunctionsSection } from './components/FunctionsSection';
import { WeddingStory } from './components/WeddingStory';
import { VenuesSection } from './components/VenuesSection';
import { FamilySection } from './components/FamilySection';
import { WeddingFilmSection } from './components/WeddingFilmSection';
import { Footer } from './components/Footer';
import { MusicPlayer } from './components/MusicPlayer';
import { ScrollCompanion } from './components/ScrollCompanion';

export const App: React.FC = () => {
  const [hasOpenedInvitation, setHasOpenedInvitation] = useState(false);
  const [isPlayingMusic, setIsPlayingMusic] = useState(false);
  const wasMusicPlayingBeforeVideoRef = useRef(false);

  // Lock background scroll when the digital invitation cover is closed
  useEffect(() => {
    if (!hasOpenedInvitation) {
      document.body.style.overflow = 'hidden';
      document.documentElement.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = '';
      document.documentElement.style.overflow = '';
    }
    return () => {
      document.body.style.overflow = '';
      document.documentElement.style.overflow = '';
    };
  }, [hasOpenedInvitation]);

  const handleOpenInvitation = () => {
    setHasOpenedInvitation(true);
    setIsPlayingMusic(true);
  };

  const handleToggleMusic = () => {
    setIsPlayingMusic((prev) => !prev);
  };

  // When inner wedding video starts playing:
  // Outer site background music/audio gets paused completely!
  const handleVideoPlay = () => {
    if (isPlayingMusic) {
      wasMusicPlayingBeforeVideoRef.current = true;
      setIsPlayingMusic(false);
    }
  };

  // When inner wedding video is paused or finishes:
  // Outer site background music resumes if it was previously playing
  const handleVideoPause = () => {
    if (wasMusicPlayingBeforeVideoRef.current) {
      setIsPlayingMusic(true);
      wasMusicPlayingBeforeVideoRef.current = false;
    }
  };

  return (
    <div className="min-h-screen bg-[#FFFDF9] text-[#2D1E18] relative selection:bg-gold selection:text-white overflow-x-hidden w-full max-w-full">
      {/* 1. Opening Digital Invitation Card / Envelope */}
      {!hasOpenedInvitation && (
        <InvitationCover onOpen={handleOpenInvitation} />
      )}

      {/* 2. Floating Rose Petals & Golden Sparkles Animation */}
      <PetalBackground />

      {/* 3. Floating Navigation Bar */}
      <Navbar
        isPlaying={isPlayingMusic}
        onToggleMusic={handleToggleMusic}
      />

      {/* 4. Main Royal Hero Section & Live Countdown */}
      <main>
        <Hero />

        {/* 5. Auspicious Ceremonies & Functions */}
        <FunctionsSection />

        {/* 6. Two Hearts, One Journey Story */}
        <WeddingStory />

        {/* 7. Wedding Venues & Google Maps */}
        <VenuesSection />

        {/* 8. Family & Ancestral Blessings */}
        <FamilySection />

        {/* 9. Destination Wedding Film with Automatic Background Audio Coordination */}
        <WeddingFilmSection
          isPlayingSiteMusic={isPlayingMusic}
          onVideoPlay={handleVideoPlay}
          onVideoPause={handleVideoPause}
        />
      </main>

      {/* 10. Concluding Royal Footer */}
      <Footer />

      {/* 11. Floating Background Music Player */}
      <MusicPlayer
        isPlaying={isPlayingMusic}
        onToggle={handleToggleMusic}
      />

      {/* 12. Floating Quick Scroll Companion */}
      <ScrollCompanion />
    </div>
  );
};

export default App;
