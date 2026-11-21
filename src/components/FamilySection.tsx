import React from 'react';
import { motion } from 'framer-motion';
import { Sparkles, Heart, ChevronDown } from 'lucide-react';
import { FAMILY_DETAILS, WEDDING_COUPLE } from '../data/weddingData';

export const FamilySection: React.FC = () => {
  const scrollToFilm = () => {
    document.querySelector('#film')?.scrollIntoView({ behavior: 'smooth' });
  };

  return (
    <section id="family" className="relative py-20 bg-[#FFFDF9] border-t border-gold/30 overflow-hidden">
      <div className="max-w-5xl mx-auto px-4 sm:px-6">
        {/* Section Header */}
        <div className="text-center max-w-2xl mx-auto mb-14">
          <div className="flex items-center justify-center gap-2 mb-2 text-burgundy font-serif font-bold text-sm tracking-widest uppercase">
            <span className="text-gold">✦</span>
            <span>Family &amp; Ancestral Blessings</span>
            <span className="text-gold">✦</span>
          </div>

          <h2 className="font-serif font-bold text-3xl sm:text-5xl text-burgundy tracking-tight">
            With Love &amp; Gratitude
          </h2>

          <p className="font-cormorant italic text-base sm:text-lg text-[#6E4F41] mt-2 font-medium">
            “We request your gracious presence &amp; blessings on the auspicious occasion of the wedding celebration of our beloved children.”
          </p>

          <div className="flex items-center justify-center w-36 mx-auto mt-4">
            <div className="h-[1px] flex-1 bg-gradient-to-r from-transparent via-gold to-transparent" />
            <span className="mx-2 text-gold text-xs">🪷</span>
            <div className="h-[1px] flex-1 bg-gradient-to-r from-transparent via-gold to-transparent" />
          </div>
        </div>

        {/* Two Families Arched Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 items-stretch overflow-hidden">
          {/* Bride's Family (Sikaria Family) */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.7 }}
            className="relative rounded-2xl p-7 sm:p-9 bg-ivory border-2 border-gold/60 shadow-xl text-center flex flex-col justify-between"
          >
            {/* Inner dashed gold frame */}
            <div className="absolute inset-2 border border-dashed border-gold/30 rounded-xl pointer-events-none" />

            <div>
              <div className="inline-block px-4 py-1 rounded-full bg-burgundy/10 text-burgundy font-cinzel text-xs font-bold tracking-widest mb-3">
                BRIDE&apos;S BELOVED FAMILY
              </div>

              <h3 className="font-script text-4xl sm:text-5xl text-gold font-normal my-2">
                {FAMILY_DETAILS.bride.name}
              </h3>

              <div className="my-5 space-y-3 text-xs sm:text-sm text-[#4A3830]">
                <div className="p-3 rounded-xl bg-champagne/40 border border-gold/30">
                  <span className="text-[11px] font-cinzel font-bold text-burgundy tracking-wider block uppercase">
                    Parents:
                  </span>
                  <p className="font-serif font-bold text-base text-[#2E1E17] mt-0.5">
                    {FAMILY_DETAILS.bride.parents}
                  </p>
                </div>

                <div className="p-3 rounded-xl bg-white/70 border border-gold/20">
                  <span className="text-[11px] font-cinzel font-bold text-[#705549] tracking-wider block uppercase">
                    Grandparents:
                  </span>
                  <p className="font-serif font-semibold text-sm text-[#523E35] mt-0.5">
                    {FAMILY_DETAILS.bride.grandparents}
                  </p>
                </div>
              </div>
            </div>

            <p className="font-cormorant italic text-xs sm:text-sm text-[#7D5F52] mt-4 pt-4 border-t border-gold/30">
              {FAMILY_DETAILS.bride.blessingQuote}
            </p>
          </motion.div>

          {/* Groom's Family (Pandey Family) */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.7 }}
            className="relative rounded-2xl p-7 sm:p-9 bg-ivory border-2 border-gold/60 shadow-xl text-center flex flex-col justify-between"
          >
            {/* Inner dashed gold frame */}
            <div className="absolute inset-2 border border-dashed border-gold/30 rounded-xl pointer-events-none" />

            <div>
              <div className="inline-block px-4 py-1 rounded-full bg-burgundy/10 text-burgundy font-cinzel text-xs font-bold tracking-widest mb-3">
                GROOM&apos;S BELOVED FAMILY
              </div>

              <h3 className="font-script text-4xl sm:text-5xl text-gold font-normal my-2">
                {FAMILY_DETAILS.groom.name}
              </h3>

              <div className="my-5 space-y-3 text-xs sm:text-sm text-[#4A3830]">
                <div className="p-3 rounded-xl bg-champagne/40 border border-gold/30">
                  <span className="text-[11px] font-cinzel font-bold text-burgundy tracking-wider block uppercase">
                    Parents:
                  </span>
                  <p className="font-serif font-bold text-base text-[#2E1E17] mt-0.5">
                    {FAMILY_DETAILS.groom.parents}
                  </p>
                </div>

                <div className="p-3 rounded-xl bg-white/70 border border-gold/20">
                  <span className="text-[11px] font-cinzel font-bold text-[#705549] tracking-wider block uppercase">
                    Grandparents:
                  </span>
                  <p className="font-serif font-semibold text-sm text-[#523E35] mt-0.5">
                    {FAMILY_DETAILS.groom.grandparents}
                  </p>
                </div>
              </div>
            </div>

            <p className="font-cormorant italic text-xs sm:text-sm text-[#7D5F52] mt-4 pt-4 border-t border-gold/30">
              {FAMILY_DETAILS.groom.blessingQuote}
            </p>
          </motion.div>
        </div>

        {/* Scroll Option to Next Section: Film */}
        <div className="mt-14 sm:mt-16 flex justify-center">
          <button
            onClick={scrollToFilm}
            className="flex flex-col items-center gap-1.5 text-burgundy/80 hover:text-burgundy transition-colors group cursor-pointer"
          >
            <span className="font-cinzel text-xs font-semibold tracking-widest uppercase">
              Watch The Wedding Film
            </span>
            <ChevronDown className="w-4 h-4 animate-bounce text-gold" />
          </button>
        </div>
      </div>
    </section>
  );
};
