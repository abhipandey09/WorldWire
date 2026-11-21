import React from 'react';
import { motion } from 'framer-motion';
import { Calendar, MapPin, ChevronDown, Sparkles } from 'lucide-react';
import { WEDDING_COUPLE } from '../data/weddingData';
import { Countdown } from './Countdown';

export const Hero: React.FC = () => {
  const scrollToCeremonies = () => {
    const el = document.querySelector('#ceremonies');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  };

  return (
    <section id="hero" className="relative min-h-screen pt-28 pb-16 flex flex-col justify-center items-center overflow-hidden">
      {/* Background Decorative Gradients & Palace Atmosphere */}
      <div className="absolute inset-0 pointer-events-none">
        <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[500px] bg-gold/10 rounded-full blur-[140px]" />
        <div className="absolute bottom-10 left-1/4 w-[500px] h-[500px] bg-burgundy/10 rounded-full blur-[120px]" />
      </div>

      <div className="relative z-10 max-w-4xl mx-auto px-4 sm:px-6 text-center flex flex-col items-center">
        {/* Sacred Mantra Header */}
        <motion.div
          initial={{ opacity: 0, y: -15 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="flex items-center gap-2 mb-2 text-burgundy font-serif font-bold text-base sm:text-xl tracking-widest"
        >
          <span className="text-gold text-sm sm:text-base">✦</span>
          <span>{WEDDING_COUPLE.invitationMantra}</span>
          <span className="text-gold text-sm sm:text-base">✦</span>
        </motion.div>

        {/* Tagline */}
        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.2, duration: 0.8 }}
          className="font-cormorant italic text-base sm:text-lg text-[#6B5349] tracking-wider mb-2"
        >
          {WEDDING_COUPLE.tagline}
        </motion.p>

        {/* Golden Ornamental Divider */}
        <motion.div
          initial={{ scaleX: 0 }}
          animate={{ scaleX: 1 }}
          transition={{ delay: 0.3, duration: 0.8 }}
          className="flex items-center justify-center w-64 sm:w-80 my-3"
        >
          <div className="h-[1px] flex-1 bg-gradient-to-r from-transparent via-gold to-transparent" />
          <div className="mx-2 w-2 h-2 rotate-45 bg-gold" />
          <div className="h-[1px] flex-1 bg-gradient-to-r from-transparent via-gold to-transparent" />
        </motion.div>

        {/* Visual Focal Point: Regal Couple Typography */}
        <motion.div
          initial={{ opacity: 0, scale: 0.92 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: 0.4, duration: 0.9, ease: 'easeOut' }}
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
        <motion.p
          initial={{ opacity: 0, y: 15 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.6, duration: 0.8 }}
          className="max-w-xl font-cormorant text-base sm:text-xl text-[#4A3830] leading-relaxed my-4 italic px-4"
        >
          “Together with our families, we invite you to celebrate the beginning of our forever.”
        </motion.p>

        {/* Auspicious Dates & Location Badges */}
        <motion.div
          initial={{ opacity: 0, y: 15 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.7, duration: 0.8 }}
          className="flex flex-wrap items-center justify-center gap-3 sm:gap-4 my-2"
        >
          <div className="flex items-center gap-2 px-5 py-2.5 rounded-full bg-champagne/70 border border-gold/50 shadow-sm">
            <Calendar className="w-4 h-4 text-burgundy" />
            <span className="font-cinzel font-bold text-xs sm:text-sm text-burgundy tracking-wider">
              26 &amp; 27 January 2027
            </span>
          </div>

          <div className="flex items-center gap-2 px-5 py-2.5 rounded-full bg-champagne/70 border border-gold/50 shadow-sm">
            <MapPin className="w-4 h-4 text-burgundy" />
            <span className="font-cinzel font-bold text-xs sm:text-sm text-burgundy tracking-wider">
              Bengaluru, Karnataka
            </span>
          </div>
        </motion.div>

        {/* Live Dynamic Countdown Section */}
        <div className="w-full mt-8 sm:mt-12">
          <Countdown />
        </div>

        {/* Scroll Indicator */}
        <motion.button
          onClick={scrollToCeremonies}
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1, duration: 0.8 }}
          className="mt-10 sm:mt-14 flex flex-col items-center gap-1.5 text-burgundy hover:text-gold transition-colors group cursor-pointer"
        >
          <span className="font-cinzel text-xs font-semibold tracking-widest uppercase">
            Scroll to Celebrate
          </span>
          <ChevronDown className="w-4 h-4 animate-bounce text-gold" />
        </motion.button>
      </div>
    </section>
  );
};
