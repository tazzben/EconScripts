/**
 * Calculates the walk time between two locations
 *
 * @param {number, number, number, number} input the starting point and destination.
 * @customfunction
 */

function WalkTime(lat, lng, dlat, dlng) {
    var cache = CacheService.getDocumentCache();
    var cached = cache.get('walktime' + lng + '_' + lat + '_' + dlat + '_' + dlng + '_');
    if (cached != null) {
        return cached;
    }
    try {
        var directions = Maps.newDirectionFinder()
            .setOrigin(lat, lng)
            .setDestination(dlat, dlng)
            .setMode(Maps.DirectionFinder.Mode.WALKING)
            .getDirections();
        var r = directions.routes[0].legs[0].duration.text;
        cache.put('walktime' + lng + '_' + lat + '_' + dlat + '_' + dlng + '_', r, 2592000);
    } catch (e) {
        Utilities.sleep(1000);
        var r = WalkTime(lat, lng, dlat, dlng);
    }
    return r;
}

/**
 * Calculates the walk distance between two locations
 *
 * @param {number, number, number, number} input the starting point and destination.
 * @customfunction
 */

function WalkDistance(lat, lng, dlat, dlng) {
    var cache = CacheService.getDocumentCache();
    var cached = cache.get('walkdistance' + lng + '_' + lat + '_' + dlat + '_' + dlng + '_');
    if (cached != null) {
        return cached;
    }
    try {
        var directions = Maps.newDirectionFinder()
            .setOrigin(lat, lng)
            .setDestination(dlat, dlng)
            .setMode(Maps.DirectionFinder.Mode.WALKING)
            .getDirections();
        var r = directions.routes[0].legs[0].distance.text;
        cache.put('walkdistance' + lng + '_' + lat + '_' + dlat + '_' + dlng + '_', r, 2592000);
    } catch (e) {
        Utilities.sleep(1000);
        var r = WalkDistance(lat, lng, dlat, dlng);
    }
    return r;
}

/**
 * Calculates the drive time between two locations
 *
 * @param {number, number, number, number} input the starting point and destination.
 * @customfunction
 */

function DriveTime(lat, lng, dlat, dlng) {
    var cache = CacheService.getDocumentCache();
    var cached = cache.get('drivetime' + lng + '_' + lat + '_' + dlat + '_' + dlng + '_');
    if (cached != null) {
        return cached;
    }
    try {
        var directions = Maps.newDirectionFinder()
            .setOrigin(lat, lng)
            .setDestination(dlat, dlng)
            .setMode(Maps.DirectionFinder.Mode.DRIVING)
            .getDirections();
        var r = directions.routes[0].legs[0].duration.text;
        cache.put('drivetime' + lng + '_' + lat + '_' + dlat + '_' + dlng + '_', r, 2592000);
    } catch (e) {
        Utilities.sleep(1000);
        var r = DriveTime(lat, lng, dlat, dlng);
    }
    return r;
}

/**
 * Calculates the walk distance between two locations
 *
 * @param {number, number, number, number} input the starting point and destination.
 * @customfunction
 */

function WalkDistance(lat, lng, dlat, dlng) {
    var cache = CacheService.getDocumentCache();
    var cached = cache.get('drivedistance' + lng + '_' + lat + '_' + dlat + '_' + dlng + '_');
    if (cached != null) {
        return cached;
    }
    try {
        var directions = Maps.newDirectionFinder()
            .setOrigin(lat, lng)
            .setDestination(dlat, dlng)
            .setMode(Maps.DirectionFinder.Mode.DRIVING)
            .getDirections();
        var r = directions.routes[0].legs[0].distance.text;
        cache.put('drivedistance' + lng + '_' + lat + '_' + dlat + '_' + dlng + '_', r, 2592000);
    } catch (e) {
        Utilities.sleep(1000);
        var r = DriveDistance(lat, lng, dlat, dlng);
    }
    return r;
}