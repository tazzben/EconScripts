/**
 * Calculates the walk time between two locations
 *
 * @param {text, text} input the starting point and destination.
 * @customfunction
 */

function WalkTime(start, destination) {
    var cache = CacheService.getDocumentCache();
    var key = 'walktime' + start + '_' + destination + '_';
    var digest = Utilities.computeDigest(Utilities.DigestAlgorithm.MD5, key);
    var cached = cache.get(digest);
    if (cached != null) {
        return cached;
    }

    try {
        var directions = Maps.newDirectionFinder()
            .setOrigin(start)
            .setDestination(destination)
            .setMode(Maps.DirectionFinder.Mode.WALKING)
            .getDirections();
        var r = directions.routes[0].legs[0].duration.text;
        cache.put(digest, r, 2592000);
    } catch (e) {
        Utilities.sleep(1000);
        var r = WalkTime(start, destination);
    }
    return r;
}

/**
 * Calculates the drive time between two locations
 *
 * @param {text, text} input the starting point and destination.
 * @customfunction
 */

function DriveTime(start, destination) {
    var cache = CacheService.getDocumentCache();
    var key = 'drivetime' + start + '_' + destination + '_';
    var digest = Utilities.computeDigest(Utilities.DigestAlgorithm.MD5, key);
    var cached = cache.get(digest);
    if (cached != null) {
        return cached;
    }
    try {
        var directions = Maps.newDirectionFinder()
            .setOrigin(start)
            .setDestination(destination)
            .setMode(Maps.DirectionFinder.Mode.DRIVING)
            .getDirections();
        var r = directions.routes[0].legs[0].duration.text;
        cache.put(digest, r, 2592000);
        return r;
    } catch (e) {
        Utilities.sleep(1000);
        var r = DriveTime(start, destination);
    }
    return r;
}
/**
 * Calculates the walk time between two locations
 *
 * @param {text, text} input the starting point and destination.
 * @customfunction
 */

function WalkDistance(start, destination) {
    var cache = CacheService.getDocumentCache();
    var key = 'walkdistance' + start + '_' + destination + '_';
    var digest = Utilities.computeDigest(Utilities.DigestAlgorithm.MD5, key);
    var cached = cache.get(digest);
    if (cached != null) {
        return cached;
    }

    try {
        var directions = Maps.newDirectionFinder()
            .setOrigin(start)
            .setDestination(destination)
            .setMode(Maps.DirectionFinder.Mode.WALKING)
            .getDirections();
        var r = directions.routes[0].legs[0].distance.text;
        cache.put(digest, r, 2592000);
    } catch (e) {
        Utilities.sleep(1000);
        var r = WalkDistance(start, destination);
    }
    return r;
}

/**
 * Calculates the drive time between two locations
 *
 * @param {text, text} input the starting point and destination.
 * @customfunction
 */

function DriveDistance(start, destination) {
    var cache = CacheService.getDocumentCache();
    var key = 'drivedistance' + start + '_' + destination + '_';
    var digest = Utilities.computeDigest(Utilities.DigestAlgorithm.MD5, key);
    var cached = cache.get(digest);
    if (cached != null) {
        return cached;
    }
    try {
        var directions = Maps.newDirectionFinder()
            .setOrigin(start)
            .setDestination(destination)
            .setMode(Maps.DirectionFinder.Mode.DRIVING)
            .getDirections();
        var r = directions.routes[0].legs[0].distance.text;
        cache.put(digest, r, 2592000);
        return r;
    } catch (e) {
        Utilities.sleep(1000);
        var r = DriveDistance(start, destination);
    }
    return r;
}
