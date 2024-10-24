from ..constants import TIER_CONFIG, MIN_STAKE, EPOCH_LENGTH
from ..miner_utils import RateLimitCounter


def build_rate_limit(metagraph, config, tier=None):
    S = metagraph.S
    whitelist_uids = [i for i in range(len(S)) if S[i] > MIN_STAKE]
    selected_tier_config = TIER_CONFIG[tier or config.miner.tier]
    rpe = selected_tier_config["requests_per_epoch"]
    rpe_per_validator = rpe // len(whitelist_uids)
    rate_limits = {
        uid: RateLimitCounter(rpe_per_validator, EPOCH_LENGTH) for uid in whitelist_uids
    }
    for uid in range(len(S)):
        if uid not in whitelist_uids:
            rate_limits[uid] = RateLimitCounter(0, EPOCH_LENGTH)
    return rate_limits
