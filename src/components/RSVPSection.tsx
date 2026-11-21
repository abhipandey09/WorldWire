import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Phone, MessageSquare, Send, Heart, CheckCircle2 } from 'lucide-react';
import { WEDDING_COUPLE } from '../data/weddingData';

export const RSVPSection: React.FC = () => {
  const [guestName, setGuestName] = useState('');
  const [guestCount, setGuestCount] = useState('1');
  const [message, setMessage] = useState('');
  const [sentSuccess, setSentSuccess] = useState(false);

  const handleSendWhatsApp = (e: React.FormEvent) => {
    e.preventDefault();
    const text = encodeURIComponent(
      `*Wedding RSVP for Sakshi & Abhishek*\n\n` +
      `*Guest Name:* ${guestName || 'Valued Guest'}\n` +
      `*Attending Guests:* ${guestCount}\n` +
      `*Message & Blessings:* ${message || 'Heartiest congratulations to Sakshi & Abhishek!'}\n\n` +
      `Sent from mytomboy360.com`
    );
    window.open(`https://wa.me/917059411938?text=${text}`, '_blank');
    setSentSuccess(true);
  };

  return (
    <section id="rsvp" className="relative py-20 bg-ivory/60 border-t border-gold/30">
      <div className="max-w-4xl mx-auto px-4 sm:px-6">
        {/* Section Header */}
        <div className="text-center max-w-xl mx-auto mb-12">
          <div className="flex items-center justify-center gap-2 mb-2 text-burgundy font-serif font-bold text-sm tracking-widest uppercase">
            <span className="text-gold">✦</span>
            <span>RSVP &amp; Blessings</span>
            <span className="text-gold">✦</span>
          </div>

          <h2 className="font-serif font-bold text-3xl sm:text-5xl text-burgundy tracking-tight">
            Celebrate With Us
          </h2>

          <p className="font-cormorant italic text-base sm:text-lg text-[#6E4F41] mt-2">
            Your gracious presence will blossom our celebrations into cherished memories for a lifetime.
          </p>

          <div className="flex items-center justify-center w-36 mx-auto mt-4">
            <div className="h-[1px] flex-1 bg-gradient-to-r from-transparent via-gold to-transparent" />
            <span className="mx-2 text-gold text-xs">💌</span>
            <div className="h-[1px] flex-1 bg-gradient-to-r from-transparent via-gold to-transparent" />
          </div>
        </div>

        {/* Contact & RSVP Card Container */}
        <div className="grid grid-cols-1 md:grid-cols-5 gap-8 items-stretch">
          {/* Direct Contact Person Card */}
          <motion.div
            initial={{ opacity: 0, x: -20 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6 }}
            className="md:col-span-2 rounded-2xl p-6 sm:p-8 bg-ivory border-2 border-gold/60 shadow-lg flex flex-col justify-between text-center"
          >
            <div>
              <span className="font-cinzel text-xs font-bold tracking-widest text-burgundy uppercase block mb-2">
                RSVP &amp; HOSPITALITY DESK
              </span>

              <h3 className="font-serif font-bold text-2xl text-burgundy mt-1">
                {WEDDING_COUPLE.rsvpContact.name}
              </h3>
              <p className="text-xs text-[#705549] font-sans mt-0.5 mb-6">
                For guest assistance, travel &amp; hospitality queries
              </p>

              <div className="p-4 rounded-xl bg-champagne/40 border border-gold/40 my-4 text-center">
                <span className="text-[11px] font-cinzel font-semibold text-[#7D5F52] block uppercase">
                  Direct Phone:
                </span>
                <span className="font-cinzel font-bold text-lg text-burgundy tracking-wider block mt-1">
                  {WEDDING_COUPLE.rsvpContact.phone}
                </span>
              </div>
            </div>

            <div className="space-y-3 pt-4 border-t border-gold/30">
              <a
                href={`tel:${WEDDING_COUPLE.rsvpContact.cleanPhone}`}
                className="w-full flex items-center justify-center gap-2 px-5 py-3 rounded-xl bg-burgundy hover:bg-burgundy/90 text-white font-cinzel font-bold text-xs tracking-wider shadow-md hover:scale-[1.02] active:scale-[0.98] transition-all"
              >
                <Phone className="w-4 h-4 text-gold" />
                <span>Call {WEDDING_COUPLE.rsvpContact.name}</span>
              </a>

              <a
                href={`https://wa.me/917059411938?text=${encodeURIComponent('Hello Dipesh, I am contacting you regarding the wedding of Sakshi & Abhishek.')}`}
                target="_blank"
                rel="noopener noreferrer"
                className="w-full flex items-center justify-center gap-2 px-5 py-3 rounded-xl bg-[#25D366] hover:bg-[#20BD5A] text-white font-cinzel font-bold text-xs tracking-wider shadow-md hover:scale-[1.02] active:scale-[0.98] transition-all"
              >
                <MessageSquare className="w-4 h-4 text-white" />
                <span>Chat on WhatsApp</span>
              </a>
            </div>
          </motion.div>

          {/* Interactive Send Blessings & RSVP Form */}
          <motion.div
            initial={{ opacity: 0, x: 20 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6 }}
            className="md:col-span-3 rounded-2xl p-6 sm:p-8 bg-ivory border-2 border-gold/60 shadow-lg flex flex-col justify-between"
          >
            <div>
              <div className="flex items-center gap-2 mb-2 text-burgundy">
                <Heart className="w-4 h-4 text-gold fill-gold" />
                <span className="font-cinzel font-bold text-xs tracking-wider uppercase">
                  Confirm Your Presence / Send Blessings
                </span>
              </div>
              <h3 className="font-serif font-bold text-2xl text-burgundy mb-4">
                We Look Forward to Welcoming You
              </h3>

              {sentSuccess ? (
                <div className="p-6 rounded-xl bg-emerald-50 border border-emerald-300 text-center text-emerald-900 my-4">
                  <CheckCircle2 className="w-10 h-10 text-emerald-600 mx-auto mb-2" />
                  <h4 className="font-serif font-bold text-lg">Thank You!</h4>
                  <p className="text-xs sm:text-sm text-emerald-700 mt-1">
                    Your message has been opened in WhatsApp to send to the host family.
                  </p>
                  <button
                    onClick={() => setSentSuccess(false)}
                    className="mt-4 px-4 py-1.5 rounded-full bg-emerald-700 text-white text-xs font-cinzel font-semibold"
                  >
                    Send another message
                  </button>
                </div>
              ) : (
                <form onSubmit={handleSendWhatsApp} className="space-y-4">
                  <div>
                    <label className="block text-xs font-cinzel font-bold text-burgundy mb-1 uppercase">
                      Your Full Name:
                    </label>
                    <input
                      type="text"
                      required
                      placeholder="e.g. Rajesh Kumar & Family"
                      value={guestName}
                      onChange={(e) => setGuestName(e.target.value)}
                      className="w-full px-4 py-2.5 rounded-xl bg-white border border-gold/40 text-sm text-[#2E1E17] focus:outline-none focus:ring-2 focus:ring-gold/60"
                    />
                  </div>

                  <div>
                    <label className="block text-xs font-cinzel font-bold text-burgundy mb-1 uppercase">
                      Number of Attending Guests:
                    </label>
                    <select
                      value={guestCount}
                      onChange={(e) => setGuestCount(e.target.value)}
                      className="w-full px-4 py-2.5 rounded-xl bg-white border border-gold/40 text-sm text-[#2E1E17] focus:outline-none focus:ring-2 focus:ring-gold/60"
                    >
                      <option value="1">1 Guest</option>
                      <option value="2">2 Guests</option>
                      <option value="3 to 4">3 – 4 Guests</option>
                      <option value="Family (5+)">Family (5+ Guests)</option>
                    </select>
                  </div>

                  <div>
                    <label className="block text-xs font-cinzel font-bold text-burgundy mb-1 uppercase">
                      Warm Wishes / Blessings for the Couple:
                    </label>
                    <textarea
                      rows={3}
                      placeholder="Write your heartfelt blessing for Sakshi & Abhishek..."
                      value={message}
                      onChange={(e) => setMessage(e.target.value)}
                      className="w-full px-4 py-2.5 rounded-xl bg-white border border-gold/40 text-sm text-[#2E1E17] focus:outline-none focus:ring-2 focus:ring-gold/60"
                    />
                  </div>

                  <button
                    type="submit"
                    className="w-full flex items-center justify-center gap-2 px-6 py-3.5 rounded-xl bg-gradient-to-r from-burgundy via-[#991535] to-burgundy hover:shadow-gold-glow text-white font-cinzel font-bold text-xs tracking-wider shadow-md hover:scale-[1.01] active:scale-[0.99] transition-all"
                  >
                    <Send className="w-4 h-4 text-gold" />
                    <span>CONFIRM RSVP VIA WHATSAPP</span>
                  </button>
                </form>
              )}
            </div>
          </motion.div>
        </div>
      </div>
    </section>
  );
};
