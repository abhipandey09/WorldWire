import React, { useState } from 'react';
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

export const App: React.FC = () => {
  const [hasOpenedInvitation, setHasOpenedInvitation] = useState(false);
  const [isPlayingMusic, setIsPlayingMusic] = useState(false);

  const handleOpenInvitation = () => {
    setHasOpenedInvitation(true);
    setIsPlayingMusic(true);
  };

  const handleToggleMusic = () => {
    setIsPlayingMusic((prev) => !prev);
  };

  return (
    <div className="min-h-screen bg-[#FFFDF9] text-[#2D1E18] relative selection:bg-gold selection:text-white">
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

        {/* 9. Destination Wedding Film */}
        <WeddingFilmSection />
      </main>

      {/* 10. Concluding Royal Footer */}
      <Footer />

      {/* 11. Floating Background Music Player */}
      <MusicPlayer
        isPlaying={isPlayingMusic}
        onToggle={handleToggleMusic}
      />
    </div>
  );
};

export default App;
