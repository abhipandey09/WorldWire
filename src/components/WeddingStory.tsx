import React from 'react';
import { motion } from 'framer-motion';
import { Heart, Sparkles, Infinity, Home, ChevronDown } from 'lucide-react';
import { STORY_MILESTONES, WEDDING_COUPLE } from '../data/weddingData';

export const WeddingStory: React.FC = () => {
  const getIcon = (type: string) => {
    switch (type) {
      case 'heart':
        return <Heart className="w-5 h-5 text-gold" />;
      case 'home':
        return <Home className="w-5 h-5 text-gold" />;
      case 'infinity':
      default:
        return <Infinity className="w-5 h-5 text-gold" />;
    }
  };

  const scrollToVenues = () => {
    document.querySelector('#venues')?.scrollIntoView({ behavior: 'smooth' });
  };

  return (
    <section id="story" className="relative py-20 bg-ivory/40 border-t border-gold/30 overflow-hidden">
      {/* Personalized Couple Photo Background: Romantic Heart at Lake */}
      <div className="absolute inset-0 pointer-events-none overflow-hidden">
        <img
          src="/assets/couple/couple_heart_lake.jpg"
          alt="Sakshi & Abhishek Love Story"
          className="w-full h-full object-cover object-center opacity-25 sm:opacity-15 filter contrast-[1.05]"
        />
        <div className="absolute inset-0 bg-gradient-to-b from-[#FFFDF9]/85 via-ivory/70 to-[#FFFDF9]/90" />
      </div>

      <div className="relative z-10 max-w-4xl mx-auto px-4 sm:px-6">
        {/* Section Header */}
        <div className="text-center max-w-xl mx-auto mb-14">
          <div className="flex items-center justify-center gap-2 mb-2 text-burgundy font-serif font-bold text-sm tracking-widest uppercase">
            <span className="text-gold">✦</span>
            <span>Our Journey</span>
            <span className="text-gold">✦</span>
          </div>

          <h2 className="font-serif font-bold text-3xl sm:text-5xl text-burgundy tracking-tight">
            Two Hearts, One Journey
          </h2>

          <p className="font-script text-3xl sm:text-4xl text-gold mt-2">
            Sakshi &amp; Abhishek
          </p>

          <p className="font-cormorant italic text-sm sm:text-base text-[#6E4F41] mt-2 font-medium">
            “You took my hand for a dance... and I chose you for a lifetime.”
          </p>

          <div className="flex items-center justify-center w-32 mx-auto mt-4">
            <div className="h-[1px] flex-1 bg-gradient-to-r from-transparent via-gold to-transparent" />
            <span className="mx-2 text-gold text-xs">❦</span>
            <div className="h-[1px] flex-1 bg-gradient-to-r from-transparent via-gold to-transparent" />
          </div>
        </div>

        {/* Vertical Royal Timeline */}
        <div className="relative">
          {/* Vertical Golden Connecting Spine */}
          <div className="absolute left-6 sm:left-1/2 top-4 bottom-4 w-[2px] bg-gradient-to-b from-transparent via-gold to-transparent -translate-x-1/2" />

          <div className="space-y-12">
            {STORY_MILESTONES.map((milestone, idx) => {
              const isEven = idx % 2 === 0;
              return (
                <motion.div
                  key={milestone.title}
                  initial={{ opacity: 0, y: 30 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.7, delay: idx * 0.15 }}
                  className={`relative flex flex-col sm:flex-row items-start sm:items-center ${
                    isEven ? 'sm:flex-row-reverse' : ''
                  }`}
                >
                  {/* Timeline Central Badge */}
                  <div className="absolute left-6 sm:left-1/2 -translate-x-1/2 w-11 h-11 rounded-full bg-burgundy border-2 border-gold flex items-center justify-center shadow-lg z-10">
                    {getIcon(milestone.icon)}
                  </div>

                  {/* Content Card */}
                  <div
                    className={`ml-11 sm:ml-0 w-[calc(100%-2.75rem)] sm:w-[calc(50%-2.5rem)] p-5 sm:p-6 rounded-2xl bg-ivory border border-gold/50 shadow-md hover:shadow-gold-glow transition-all duration-300 ${
                      isEven ? 'sm:mr-auto sm:text-right' : 'sm:ml-auto sm:text-left'
                    }`}
                  >
                    {milestone.image && (
                      <div className="mb-3.5 rounded-xl overflow-hidden border border-gold/40 shadow-sm max-h-44 sm:max-h-52">
                        <img
                          src={milestone.image}
                          alt={milestone.heading}
                          className="w-full h-36 sm:h-44 object-cover hover:scale-105 transition-transform duration-500"
                        />
                      </div>
                    )}
                    <span className="font-cinzel text-xs font-bold text-gold tracking-widest uppercase block mb-1">
                      {milestone.title}
                    </span>
                    <h3 className="font-serif font-bold text-xl sm:text-2xl text-burgundy mb-2">
                      {milestone.heading}
                    </h3>
                    <p className="font-cormorant text-sm sm:text-base text-[#4E3A32] leading-relaxed">
                      {milestone.description}
                    </p>
                  </div>
                </motion.div>
              );
            })}
          </div>
        </div>

        {/* Scroll Option to Next Section: Venues */}
        <div className="mt-14 sm:mt-16 flex justify-center">
          <button
            onClick={scrollToVenues}
            className="flex flex-col items-center gap-1.5 text-burgundy/80 hover:text-burgundy transition-colors group cursor-pointer"
          >
            <span className="font-cinzel text-xs font-semibold tracking-widest uppercase">
              Explore Wedding Venues
            </span>
            <ChevronDown className="w-4 h-4 animate-bounce text-gold" />
          </button>
        </div>
      </div>
    </section>
  );
};
