import React from 'react';
import { motion } from 'framer-motion';
import { Calendar, MapPin, ChevronDown } from 'lucide-react';
import { WEDDING_COUPLE } from '../data/weddingData';
import { Countdown } from './Countdown';

export const Hero: React.FC = () => {
  const scrollToCeremonies = () => {
    const el = document.querySelector('#ceremonies');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  };

  return (
    <section id="hero" className="relative min-h-screen pt-28 pb-16 flex flex-col justify-center items-center overflow-hidden">
      {/* Background Royal Palace Courtyard & Luminous Silk Atmosphere */}
      <div
        className="absolute inset-0 bg-cover bg-center pointer-events-none opacity-60 transition-opacity duration-1000"
        style={{ backgroundImage: `url('/assets/landing_hero_bg.jpg')` }}
      />

      {/* Personalized Couple Photo Background: Romantic Embrace */}
      <div className="absolute inset-0 pointer-events-none overflow-hidden">
        <img
          src="/assets/couple/couple_romantic_embrace.jpg"
          alt="Sakshi & Abhishek"
          className="w-full h-full object-cover object-top opacity-30 sm:opacity-20 filter contrast-[1.05]"
        />
        <div className="absolute inset-0 bg-gradient-to-b from-[#FFFDF9]/80 via-[#FFFDF9]/55 to-[#FFFDF9]/90" />
      </div>

      {/* Delicate Royal Mandala Watermark Pattern */}
      <div
        className="absolute inset-0 pointer-events-none opacity-[0.035] bg-repeat"
        style={{ backgroundImage: `url('/assets/royal_mandala_pattern.png')` }}
      />

      {/* Ambient Lighting & Top Golden Radiance */}
      <div className="absolute inset-0 pointer-events-none overflow-hidden">
        <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[340px] sm:w-[900px] h-[350px] sm:h-[550px] bg-gold/20 rounded-full blur-[90px] sm:blur-[140px]" />
        <div className="absolute bottom-10 left-1/4 w-[280px] sm:w-[500px] h-[280px] sm:h-[500px] bg-burgundy/10 rounded-full blur-[80px] sm:blur-[120px]" />
      </div>

      <div className="relative z-10 max-w-4xl mx-auto px-4 sm:px-6 text-center flex flex-col items-center">
        {/* Sacred Mantra Header */}
        <div className="flex items-center gap-2 mb-2 text-burgundy font-serif font-bold text-base sm:text-xl tracking-widest">
          <span className="text-gold text-sm sm:text-base">✦</span>
          <span>{WEDDING_COUPLE.invitationMantra}</span>
          <span className="text-gold text-sm sm:text-base">✦</span>
        </div>

        {/* Tagline */}
        <p className="font-cormorant italic text-base sm:text-lg text-[#6B5349] tracking-wider mb-2 font-medium">
          {WEDDING_COUPLE.tagline}
        </p>

        {/* Golden Ornamental Divider */}
        <div className="flex items-center justify-center w-64 sm:w-80 my-3">
          <div className="h-[1px] flex-1 bg-gradient-to-r from-transparent via-gold to-transparent" />
          <div className="mx-2 w-2 h-2 rotate-45 bg-gold" />
          <div className="h-[1px] flex-1 bg-gradient-to-r from-transparent via-gold to-transparent" />
        </div>

        {/* Visual Focal Point: Regal Couple Typography */}
        <motion.div
          initial={{ opacity: 0.95, scale: 0.98 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.4, ease: 'easeOut' }}
          className="my-3 sm:my-4"
        >
          <h1 className="font-script text-6xl sm:text-8xl md:text-9xl text-gold font-normal leading-none drop-shadow-md tracking-tight">
            Sakshi
          </h1>
          <div className="my-1 sm:my-2 flex items-center justify-center gap-3">
            <span className="h-[1px] w-12 sm:w-20 bg-gold/50" />
            <span className="font-serif italic text-2xl sm:text-4xl text-burgundy font-bold">&amp;</span>
            <span className="h-[1px] w-12 sm:w-20 bg-gold/50" />
          </div>
          <h1 className="font-script text-6xl sm:text-8xl md:text-9xl text-gold font-normal leading-none drop-shadow-md tracking-tight">
            Abhishek
          </h1>
        </motion.div>

        {/* Invitation Text */}
        <p className="max-w-xl font-cormorant text-base sm:text-xl text-[#4A3830] leading-relaxed my-4 italic px-4 font-medium">
          “Together with our families, we invite you to celebrate the beginning of our forever.”
        </p>

        {/* Auspicious Dates & Location Badges */}
        <div className="flex flex-wrap items-center justify-center gap-3 sm:gap-4 my-2">
          <div className="flex items-center gap-2 px-5 py-2.5 rounded-full bg-champagne/80 border border-gold/50 shadow-sm">
            <Calendar className="w-4 h-4 text-burgundy" />
            <span className="font-cinzel font-bold text-xs sm:text-sm text-burgundy tracking-wider">
              26 &amp; 27 January 2027
            </span>
          </div>

          <div className="flex items-center gap-2 px-5 py-2.5 rounded-full bg-champagne/80 border border-gold/50 shadow-sm">
            <MapPin className="w-4 h-4 text-burgundy" />
            <span className="font-cinzel font-bold text-xs sm:text-sm text-burgundy tracking-wider">
              Bengaluru, Karnataka
            </span>
          </div>
        </div>

        {/* Live Dynamic Countdown Section */}
        <div className="w-full mt-8 sm:mt-12">
          <Countdown />
        </div>

        {/* Scroll Indicator */}
        <button
          onClick={scrollToCeremonies}
          className="mt-10 sm:mt-14 flex flex-col items-center gap-1.5 text-burgundy hover:text-gold transition-colors group cursor-pointer"
        >
          <span className="font-cinzel text-xs font-semibold tracking-widest uppercase">
            Scroll to Celebrate
          </span>
          <ChevronDown className="w-4 h-4 animate-bounce text-gold" />
        </button>
      </div>
    </section>
  );
};
