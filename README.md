# Yankee Houses
A New England-themed house replacement set.

## Coding ideas

#### Road adjacency check

Use one shared switch which controls the template in use. The sprite has already been selected, now choose where on the sprite sheet to draw.

	switch (FEAT_HOUSES, SELF, switch_road_adjacency, ((nearby_tile_class(1,0) == TILE_CLASS_ROAD) * 1) + ((nearby_tile_class(-1,0) == TILE_CLASS_ROAD) * 2) + ((nearby_tile_class(0,1) == TILE_CLASS_ROAD) * 4) + ((nearby_tile_class(0,-1) == TILE_CLASS_ROAD) * 8) ) {
		0: sprite_no_road // diagonal or otherwise
		1: template_W;
		2..3: template_N;
		4..8: template_E;
		8..15: template_S;
	}
	
## Planned houses

### Residential
- Low density R-1 / single-family houses
  - Townzones: all but center
  - May not build adjacent to Industrial
  
- Medium density R-2 / multi-family houses (including triple-deckers)
  - Townzones: center, inner suburbs, outer suburbs
  - Transit service not required
  - When transit service is provided, do not allow in center and shorten lifespan (use protection callback to check age instead of minimum lifespan)
  - Okay adjacent to Industrial
  
- High density R-3 / high-rise apartments
  - Townzones: all
  - Requires passenger service
  - Era changes: tenements > public housing towers > luxury apartments
  - May not build adjacent to Industrial

### Commercial
- Low density (C-1) / rural shops
  - Townzones: edge, outskirt
- Medium density (C-2) / suburban sprawl shops and urban
  - Townzones: inner/outer suburb, outskirt, edge
  - 
- High density (C-3) / offices
  - Townzones: all
  - Requires passenger service
  - Skyscrapers and other towers
    - Only allow one landmark tower per map

### Light industrial
- Low density only (I-1)
- Townzones: outer suburbs, outskirts, edge
- May not be adjacent to R-1
- Accepts Goods

### University
- Central building requires is_city and/or >= N population
- All other buildings must be within N tiles to central building
  - class buildings
  - dorms
  - power plant (?)
  - quads
- Consider multiple incompatible architectural styles (different central building) to make universities look different per city

### Historic downtown
- Identical to early buildings, but only allowed during map generation, and protected from redevelopment
- Centers around historic church (or similar), as in Improved Town Layouts

### Churches
- Draw a variety, including rural and urban (with appropriate townzones)
- Require a 

### Landmarks
- Museum of Science
- 

### To sort
- Hospitals and medical areas
  - Some cities are hosital hubs?
- Schools
