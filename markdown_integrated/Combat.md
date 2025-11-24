## Description

This document details the mechanics and settings related to combat within SphereServer.

## Combat Mechanics

-   **Animation Duration**: By default, the combat swing animation has a fixed duration of 1 second. After the animation, the character waits for a recoil time before starting another combat swing. This mimics OSI style combat.
-   **Combat Swing Process**:
    1.  A timer is started to wait for the recoil time (accessible via `ARGN1` in the `@HitTry` trigger).
    2.  Once the recoil timer ends, the combat swing animation begins. A second timer is started, equal to the animation duration (`LOCAL.AnimDelay` in `@HitTry`, default 1 second).
    3.  After the animation timer ends, the damage is dealt.

## Combat Flags (sphere.ini)

-   **`COMBAT_PREHIT`**: The hit animation now starts *after* the damage has been dealt.
-   **`COMBAT_ANIM_HIT_SMOOTH`**: Enables the old smooth combat animation. If enabled, there's no delay between hits (`LOCAL.AnimDelay` in `@HitTry` is 0), but the swing animation duration (`ARGN1` in `@HitTry`) equals the delay before a new swing could start.
-   **`COMBAT_SWING_NORANGE`**: (Renamed from `COMBAT_PREHIT_NORANGE`) Allows starting a close-combat swing at a distance; the blow is landed only when entering range.
-   **`COMBAT_FIRSTHIT_INSTANT`**: Makes the first hit in a combat instant (0 delay). To mimic OSI combat, both `COMBAT_PREHIT` and `COMBAT_FIRSTHIT_INSTANT` should be enabled.
-   **`COMBATF_NOPETDESERT`**: Allows a pet owner to attack their own pet without the pet deserting them (OSI-like).

## Related Triggers

-   [`@HitTry`](./HitTry.md)
-   [`@HitCheck`](./HitCheck.md)

## Notes
- The old HitChance formula can be re-enabled under `CombatDamageEra = 0`.
- Hits are now correctly canceled when going out of range if `COMBAT_STAYINRANGE` is disabled.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Game Mechanics](./CategoryGame_Mechanics.md)