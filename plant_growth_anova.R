# ============================================================
# Plant Growth Treatment Study
# One-Way ANOVA & Tukey HSD Analysis
# ============================================================

# 1. Load PlantGrowth Dataset
data("PlantGrowth")

# 2. View the Dataset
PlantGrowth

# 3. Basic Summary of the Dataset
summary(PlantGrowth)

# 4. Descriptive Statistics
aggregate(weight ~ group, data = PlantGrowth, FUN = mean)
aggregate(weight ~ group, data = PlantGrowth, FUN = sd)
aggregate(weight ~ group, data = PlantGrowth, FUN = length)
aggregate(weight ~ group, data = PlantGrowth, FUN = median)

# 5. Boxplot Visualization
boxplot(weight ~ group,
        data = PlantGrowth,
        main = "Plant Growth Treatment Study",
        xlab = "Treatment Group",
        ylab = "Yield Weight",
        col = c("#2E7D6B", "#6FA8DC", "#9B8ACB"))

# 6. One-Way ANOVA
model <- aov(weight ~ group, data = PlantGrowth)
summary(model)

# 7. Tukey HSD Post-Hoc Test
TukeyHSD(model)