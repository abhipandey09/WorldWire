import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Sparkles, Heart } from 'lucide-react';
import confetti from 'canvas-confetti';
import { WEDDING_COUPLE } from '../data/weddingData';

interface InvitationCoverProps {
  onOpen: () => void;
}

export const InvitationCover: React.FC<InvitationCoverProps> = ({ onOpen }) => {
  const [isOpening, setIsOpening] = useState(false);

  const handleOpenInvitation = () => {
    setIsOpening(true);

    // Launch luxury gold & rose confetti burst
    confetti({
      particleCount: 100,
      spread: 110,
      origin: { y: 0.6 },
      colors: ['#C6A15B', '#800020', '#FFF8E8', '#D98B9C', '#FDB813']
    });

    setTimeout(() => {
      onOpen();
    }, 800);
  };

  return (
    <AnimatePresence>
      <motion.div
        className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 overflow-hidden select-none"
        initial={{ opacity: 1 }}
        exit={{ opacity: 0, scale: 1.05, transition: { duration: 0.8, ease: 'easeInOut' } }}
      >
        {/* 1. Grand Royal Indian Silk Velvet & Candlelight Backdrop */}
        <div
          className="absolute inset-0 bg-cover bg-center pointer-events-none transform scale-105 transition-transform duration-1000"
          style={{ backgroundImage: `url('/assets/landing_cover_backdrop.jpg')` }}
        />

        {/* 2. Floating Ambient Rose & Marigold Petals + Golden Sparkles */}
        <div className="absolute inset-0 pointer-events-none overflow-hidden">
          {[...Array(16)].map((_, i) => (
            <motion.div
              key={i}
              className="absolute rounded-full"
              style={{
                width: i % 2 === 0 ? '14px' : '9px',
                height: i % 2 === 0 ? '20px' : '14px',
                left: `${(i * 6.5 + 3) % 96}%`,
                top: `-24px`,
                backgroundColor: i % 3 === 0 ? '#C6A15B' : i % 3 === 1 ? '#D98B9C' : '#E69500',
                opacity: 0.55,
                filter: 'blur(0.4px)',
              }}
              animate={{
                y: ['0vh', '105vh'],
                x: [0, (i % 2 === 0 ? 35 : -35), 0],
                rotate: [0, 360],
              }}
              transition={{
                duration: 8 + (i % 5) * 2,
                repeat: Infinity,
                ease: 'linear',
                delay: (i * 0.6) % 6,
              }}
            />
          ))}
        </div>

        {/* 3. Royal Indian Invitation Card (Mehrab Arched Sanctuary) */}
        <motion.div
          className="relative w-full max-w-md sm:max-w-lg bg-[#FFFDF7] rounded-t-[75px] sm:rounded-t-[95px] rounded-b-3xl shadow-[0_25px_60px_-10px_rgba(30,5,15,0.75)] overflow-hidden border-2 border-gold/80 z-10"
          initial={{ y: 20, opacity: 0.95, scale: 0.98 }}
          animate={{
            y: 0,
            opacity: 1,
            scale: 1,
            rotateX: isOpening ? -16 : 0,
            transformPerspective: 1000
          }}
          transition={{ duration: 0.5, ease: 'easeOut' }}
        >
          {/* Subtle Royal Mandala Watermark Pattern */}
          <div
            className="absolute inset-0 pointer-events-none opacity-[0.035] bg-repeat"
            style={{ backgroundImage: `url('/assets/royal_mandala_pattern.png')` }}
          />

          {/* Double Gold Foil Arched Inset Borders */}
          <div className="absolute inset-2.5 sm:inset-3 border border-gold/50 rounded-t-[65px] sm:rounded-t-[85px] rounded-b-2xl pointer-events-none" />
          <div className="absolute inset-4 sm:inset-5 border border-dashed border-gold/35 rounded-t-[55px] sm:rounded-t-[75px] rounded-b-xl pointer-events-none" />

          {/* Corner Traditional Flourishes */}
          <div className="absolute top-4 left-4 text-gold/60 text-lg select-none">❧</div>
          <div className="absolute top-4 right-4 text-gold/60 text-lg select-none rotate-90">❧</div>
          <div className="absolute bottom-3 left-4 text-gold/60 text-lg select-none -rotate-90">❧</div>
          <div className="absolute bottom-3 right-4 text-gold/60 text-lg select-none rotate-180">❧</div>

          {/* Card Content Interior */}
          <div className="relative z-10 px-5 pt-8 pb-7 sm:px-9 sm:pt-10 sm:pb-9 text-center flex flex-col items-center">
            
            {/* Sacred Mantra Header */}
            <div className="text-burgundy font-serif font-bold text-base sm:text-xl tracking-widest uppercase mb-1 drop-shadow-sm">
              ॥ {WEDDING_COUPLE.invitationMantra.replace(/^[|॥\s]+|[|॥\s]+$/g, '')} ॥
            </div>

            {/* Sacred Shree Ganesh Ji Arched Shrine Frame */}
            <div className="relative my-2 sm:my-3 w-36 h-44 sm:w-44 sm:h-52 rounded-t-full rounded-b-2xl p-1 bg-gradient-to-b from-gold via-gold/50 to-burgundy/40 shadow-lg">
              <div className="w-full h-full rounded-t-full rounded-b-xl overflow-hidden border-2 border-gold/70 bg-[#FFFDF9] shadow-inner flex items-center justify-center">
                <img
                  src="/assets/ganesh_shrine.jpg"
                  alt="Lord Ganesha"
                  className="w-full h-full object-cover object-center transform hover:scale-105 transition-transform duration-700"
                />
              </div>
            </div>

            {/* Invitation Opening Salutation */}
            <p className="font-cormorant italic text-sm sm:text-base text-[#6B5044] mt-1 mb-0.5 font-medium">
              Together with their families
            </p>
            <p className="font-cinzel text-[10.5px] sm:text-xs tracking-[0.22em] text-burgundy font-bold mb-2">
              CORDIALLY INVITE YOU TO CELEBRATE THE WEDDING OF
            </p>

            {/* Golden Ornamental Flourish Divider */}
            <div className="flex items-center justify-center w-52 sm:w-64 my-1">
              <div className="h-[1px] flex-1 bg-gradient-to-r from-transparent via-gold to-transparent" />
              <span className="mx-2 text-gold text-xs">✦ ❖ ✦</span>
              <div className="h-[1px] flex-1 bg-gradient-to-r from-transparent via-gold to-transparent" />
            </div>

            {/* Regal Couple Names in Shimmering Gold Script Calligraphy */}
            <div className="my-1 sm:my-2">
              <h1 className="font-script text-4xl sm:text-5xl md:text-6xl text-gold font-normal leading-tight drop-shadow-[0_2px_4px_rgba(198,161,91,0.25)]">
                Sakshi <span className="font-serif italic text-2xl sm:text-3xl text-burgundy/85 mx-1">&amp;</span> Abhishek
              </h1>
            </div>

            {/* Auspicious Dates & Location Badge */}
            <div className="mt-2.5 inline-flex items-center gap-2 px-4 sm:px-5 py-1.5 rounded-full bg-champagne/80 border border-gold/40 shadow-sm">
              <span className="font-cinzel font-bold text-xs sm:text-sm text-burgundy tracking-wider">
                {WEDDING_COUPLE.weddingDate}
              </span>
              <span className="text-gold/70 text-xs">✦</span>
              <span className="font-sans text-xs text-[#5C453C] font-medium">
                {WEDDING_COUPLE.location}
              </span>
            </div>

            {/* Interactive Royal Wax Seal Button */}
            <div className="mt-6 sm:mt-7 flex flex-col items-center">
              <motion.button
                onClick={handleOpenInvitation}
                whileHover={{ scale: 1.04, boxShadow: '0 0 25px rgba(198,161,91,0.6)' }}
                whileTap={{ scale: 0.96 }}
                className="group relative flex items-center gap-2.5 px-8 py-3.5 rounded-full bg-gradient-to-r from-burgundy via-[#9B1736] to-burgundy text-white font-cinzel font-bold text-xs sm:text-sm tracking-[0.15em] shadow-xl border border-gold/70 transition-all duration-300 cursor-pointer"
              >
                <Sparkles className="w-4 h-4 text-gold group-hover:rotate-12 transition-transform duration-300" />
                <span>OPEN WEDDING INVITATION</span>
                <Heart className="w-4 h-4 text-rose-300 fill-rose-300" />
              </motion.button>

              <button
                onClick={onOpen}
                className="mt-3 text-[11px] sm:text-xs text-[#8C6D60] hover:text-burgundy underline tracking-wider font-sans transition-colors cursor-pointer"
              >
                Skip intro &amp; view details directly →
              </button>
            </div>
          </div>
        </motion.div>
      </motion.div>
    </AnimatePresence>
  );
};
