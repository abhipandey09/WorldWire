export interface WeddingEvent {
  id: string;
  name: string;
  subtitle: string;
  dateStr: string; // e.g. "Tuesday, 26 January 2027"
  timeStr: string; // e.g. "9:00 AM ONWARDS"
  isoDateTime: string; // e.g. "2027-01-26T09:00:00+05:30"
  venueId: 'imperial' | 'icon';
  venueName: string;
  venueShort: string;
  venueAddress: string;
  mapsUrl: string;
  themeColor: string; // Primary accent
  accentColor: string;
  bgGradient: string;
  textColor: string;
  quote: string;
  description: string;
  iconName: 'flower' | 'sparkles' | 'music' | 'sun' | 'ring';
  cardImage: string; // Image in /assets/cards/
}

export interface Venue {
  id: 'imperial' | 'icon';
  name: string;
  tagline: string;
  eventsHosted: string[];
  addressLine1: string;
  addressLine2: string;
  cityStateZip: string;
  fullAddress: string;
  mapsUrl: string;
  embedQuery: string;
  image?: string;
}

export interface FamilyMember {
  name: string;
  role: string;
}

export interface FamilyInfo {
  side: 'bride' | 'groom';
  name: string;
  parents: string;
  grandparents: string;
}
