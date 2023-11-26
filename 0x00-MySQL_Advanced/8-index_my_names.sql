-- An index on names table for the first letter
CREATE INDEX idx_name_first ON names (name(1));
