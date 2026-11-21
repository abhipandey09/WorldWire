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
      particleCount: 80,
      spread: 90,
      origin: { y: 0.6 },
      colors: ['#C6A15B', '#800020', '#FFF8E8', '#D98B9C', '#FDB813']
    });

    setTimeout(() => {
      onOpen();
    }, 900);
  };

  return (
    <AnimatePresence>
      <motion.div
        className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 bg-[#1A0B0E]/90 backdrop-blur-md overflow-hidden"
        initial={{ opacity: 1 }}
        exit={{ opacity: 0, scale: 1.05, transition: { duration: 0.8, ease: 'easeInOut' } }}
      >
        {/* Ambient Golden Background Glow */}
        <div className="absolute inset-0 pointer-events-none">
          <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-gold/15 rounded-full blur-[120px]" />
          <div className="absolute top-1/4 left-1/3 w-96 h-96 bg-burgundy/25 rounded-full blur-[100px]" />
        </div>

        {/* Outer Invitation Envelope / Card Container */}
        <motion.div
          className="relative w-full max-w-lg bg-ivory rounded-2xl shadow-2xl overflow-hidden border-2 border-gold/70"
          initial={{ y: 25, opacity: 0, scale: 0.96 }}
          animate={{
            y: 0,
            opacity: 1,
            scale: 1,
            rotateX: isOpening ? -15 : 0,
            transformPerspective: 1000
          }}
          transition={{ duration: 0.8, ease: 'easeOut' }}
        >
          {/* Inner Golden Filigree Inset Border */}
          <div className="absolute inset-3 sm:inset-4 border border-gold/40 rounded-xl pointer-events-none" />
          <div className="absolute inset-4 sm:inset-5 border border-dashed border-gold/30 rounded-lg pointer-events-none" />

          {/* Corner Floral Motifs */}
          <div className="absolute top-2 left-2 text-gold/40 text-xl select-none">❧</div>
          <div className="absolute top-2 right-2 text-gold/40 text-xl select-none rotate-90">❧</div>
          <div className="absolute bottom-2 left-2 text-gold/40 text-xl select-none -rotate-90">❧</div>
          <div className="absolute bottom-2 right-2 text-gold/40 text-xl select-none rotate-180">❧</div>

          {/* Card Content Area */}
          <div className="relative z-10 px-6 py-8 sm:px-10 sm:py-10 text-center flex flex-col items-center">
            {/* Sacred Mantra Header */}
            <motion.div
              initial={{ opacity: 0, y: -10 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.2 }}
              className="text-burgundy font-serif font-bold text-lg sm:text-xl tracking-wider mb-2"
            >
              {WEDDING_COUPLE.invitationMantra}
            </motion.div>

            {/* Sacred Shree Ganesh Ji Artwork */}
            <motion.div
              initial={{ scale: 0.85, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              transition={{ delay: 0.35, duration: 0.6 }}
              className="relative my-2 sm:my-3 w-28 h-28 sm:w-36 sm:h-36 rounded-full p-1 bg-gradient-to-b from-gold/50 via-gold/20 to-burgundy/30 shadow-md"
            >
              <div className="w-full h-full rounded-full overflow-hidden border-2 border-gold/80 bg-white shadow-inner flex items-center justify-center">
                <img
                  src="/assets/ganesh.jpg"
                  alt="Lord Ganesha"
                  className="w-full h-full object-cover object-center transform hover:scale-105 transition-transform duration-500"
                />
              </div>
            </motion.div>

            {/* Invitation Opening Salutation */}
            <p className="font-cormorant italic text-sm sm:text-base text-[#5C453C] mt-2 mb-1">
              Together with their families
            </p>
            <p className="font-cinzel text-xs tracking-widest text-burgundy font-semibold mb-3">
              CORDIALLY INVITE YOU TO CELEBRATE THE WEDDING OF
            </p>

            {/* Golden Divider Flourish */}
            <div className="flex items-center justify-center w-48 my-2">
              <div className="h-[1px] flex-1 bg-gradient-to-r from-transparent via-gold to-transparent" />
              <span className="mx-2 text-gold text-xs">✦</span>
              <div className="h-[1px] flex-1 bg-gradient-to-r from-transparent via-gold to-transparent" />
            </div>

            {/* Couple Names — Classical Calligraphy */}
            <div className="my-2">
              <h1 className="font-script text-4xl sm:text-5xl text-gold font-normal leading-tight drop-shadow-sm">
                Sakshi <span className="font-serif text-2xl sm:text-3xl text-burgundy/80 mx-1">&amp;</span> Abhishek
              </h1>
            </div>

            {/* Wedding Date & Location Badge */}
            <div className="mt-3 inline-flex flex-col items-center justify-center px-4 py-1.5 rounded-full bg-champagne/60 border border-gold/30">
              <span className="font-cinzel font-bold text-xs sm:text-sm text-burgundy tracking-wider">
                {WEDDING_COUPLE.weddingDate}
              </span>
              <span className="font-sans text-[11px] text-[#6E4F41]">
                {WEDDING_COUPLE.location}
              </span>
            </div>

            {/* Interactive Royal Wax Seal Button */}
            <div className="mt-7 flex flex-col items-center">
              <motion.button
                onClick={handleOpenInvitation}
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                className="group relative flex items-center gap-2.5 px-8 py-3.5 rounded-full bg-gradient-to-r from-burgundy via-[#991535] to-burgundy text-white font-cinzel font-bold text-sm tracking-wider shadow-lg hover:shadow-gold-glow transition-all duration-300 border border-gold/60"
              >
                <Sparkles className="w-4 h-4 text-gold group-hover:rotate-12 transition-transform duration-300" />
                <span>OPEN WEDDING INVITATION</span>
                <Heart className="w-4 h-4 text-rose-300 fill-rose-300" />
              </motion.button>

              <button
                onClick={onOpen}
                className="mt-3 text-xs text-[#8C6D60] hover:text-burgundy underline tracking-wider font-sans transition-colors"
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
