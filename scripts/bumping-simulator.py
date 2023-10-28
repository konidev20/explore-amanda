# Assumptions for bumping
bumpsize = 10  # MB
bumpmult = 2.0
bumpdays = 2

# Calculate backup sizes, levels, and decisions for each day
current_level = 0
days_at_current_level = 1
backup_sizes = [initial_backup_size]
backup_levels = [current_level]
decisions = ["Full Backup"]

for day in range(1, days_in_cycle):
    # Calculate potential backup size at current level and next level
    incremental_data_size = backup_sizes[-1] * change_rate
    backup_at_current_level = backup_sizes[-1] + incremental_data_size
    backup_at_next_level = backup_sizes[0] + incremental_data_size  # since last full backup
    
    # Check bumping criteria
    savings = backup_at_current_level - backup_at_next_level
    if savings >= bumpsize and days_at_current_level >= bumpdays:
        # Bump to the next level
        current_level += 1
        days_at_current_level = 1
        bumpsize *= bumpmult
        backup_sizes.append(backup_at_next_level)
        decisions.append(f"Bumped to Level {current_level}")
    else:
        # Stay at the current level
        days_at_current_level += 1
        backup_sizes.append(backup_at_current_level)
        decisions.append(f"Stayed at Level {current_level}")
        
    backup_levels.append(current_level)

backup_sizes, backup_levels, decisions
